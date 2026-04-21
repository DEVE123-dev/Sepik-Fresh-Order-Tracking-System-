"""
app.py — Sepik Fresh Tracking System
Full backend with OOP models, role-based access, session timeout,
order management, product management, and user registration.
"""
from flask import Flask, render_template, request, redirect, url_for, session, send_file, Response
import os
from config import config
from models import User, Product, Order, Customer, ContactMessage
from agents import start_agents, log_new_order
import csv
from io import StringIO, BytesIO
from datetime import datetime

# Initialize Flask app
app = Flask(__name__)

# Load configuration
env = os.environ.get('FLASK_ENV', 'development')
app.config.from_object(config[env])

# Set secret key and session lifetime
app.secret_key = app.config['SECRET_KEY']
app.permanent_session_lifetime = app.config['PERMANENT_SESSION_LIFETIME']


# ── Helpers ──────────────────────────────────────────────────

def login_required(role=None):
    """Returns redirect if not logged in or wrong role, else None."""
    if 'user_id' not in session:
        return redirect(url_for('login'))
    if role and session.get('role') != role:
        return redirect(url_for('dashboard'))
    return None


# ── Public routes ─────────────────────────────────────────────

@app.route('/')
@app.route('/home')
def home():
    # Get featured products for slideshow (products with images)
    featured_products = Product.get_available()[:6]  # Get up to 6 products for slideshow
    return render_template('home.html', featured_products=featured_products)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/sitemap.xml')
def sitemap():
    """Generate sitemap for search engines"""
    from flask import make_response
    pages = []
    
    # Static pages
    static_pages = [
        {'loc': url_for('home', _external=True), 'priority': '1.0'},
        {'loc': url_for('about', _external=True), 'priority': '0.8'},
        {'loc': url_for('contact', _external=True), 'priority': '0.7'},
        {'loc': url_for('login', _external=True), 'priority': '0.6'},
        {'loc': url_for('register', _external=True), 'priority': '0.6'},
    ]
    
    sitemap_xml = '<?xml version="1.0" encoding="UTF-8"?>\n'
    sitemap_xml += '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    
    for page in static_pages:
        sitemap_xml += '  <url>\n'
        sitemap_xml += f'    <loc>{page["loc"]}</loc>\n'
        sitemap_xml += f'    <priority>{page["priority"]}</priority>\n'
        sitemap_xml += '    <changefreq>weekly</changefreq>\n'
        sitemap_xml += '  </url>\n'
    
    sitemap_xml += '</urlset>'
    
    response = make_response(sitemap_xml)
    response.headers['Content-Type'] = 'application/xml'
    return response

@app.route('/robots.txt')
def robots():
    """Tell search engines what to crawl"""
    from flask import make_response
    robots_txt = """User-agent: *
Allow: /
Disallow: /dashboard
Disallow: /admin
Disallow: /profile
Disallow: /logout

Sitemap: {}/sitemap.xml
""".format(request.url_root.rstrip('/'))
    
    response = make_response(robots_txt)
    response.headers['Content-Type'] = 'text/plain'
    return response

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    success = error = None
    if request.method == 'POST':
        name = request.form.get('name', '').strip()
        email = request.form.get('email', '').strip()
        message = request.form.get('message', '').strip()
        
        if not name or not email or not message:
            error = 'All fields are required.'
        else:
            # Save message to database
            from models import _q
            try:
                _q(
                    "INSERT INTO contact_messages (name, email, message) VALUES (%s, %s, %s)",
                    (name, email, message),
                    commit=True
                )
                success = 'Message sent successfully! We will get back to you soon.'
            except Exception as e:
                error = 'Failed to send message. Please try again later.'
    
    return render_template('contact.html', success=success, error=error)


# ── Auth ──────────────────────────────────────────────────────

@app.route('/login', methods=['GET', 'POST'])
def login():
    if 'user_id' in session:
        return redirect(url_for('dashboard'))
    error = None
    if request.method == 'POST':
        email    = request.form['email']
        password = request.form['password']
        user = User.get_by_email(email)
        if user and User.check_password(password, user['password_hash']):
            session.permanent = True
            session['user_id']    = user['user_id']
            session['user_email'] = user['email']
            session['user_name']  = f"{user['first_name']} {user['last_name']}"
            session['role']       = user['role']
            return redirect(url_for('dashboard'))
        error = 'Invalid email or password. Please try again.'
    return render_template('login.html', error=error)


@app.route('/register', methods=['GET', 'POST'])
def register():
    error = success = None
    if request.method == 'POST':
        first    = request.form['first_name'].strip()
        last     = request.form['last_name'].strip()
        email    = request.form['email'].strip()
        phone    = request.form.get('phone', '').strip()
        address  = request.form.get('address', '').strip()
        password = request.form['password']
        confirm  = request.form['confirm_password']

        if password != confirm:
            error = 'Passwords do not match.'
        elif len(password) < 6:
            error = 'Password must be at least 6 characters.'
        elif User.get_by_email(email):
            error = 'An account with that email already exists.'
        else:
            uid = User.create(first, last, email, password, 'customer', phone, address)
            Customer.create(uid)
            success = 'Account created! You can now log in.'
    return render_template('register.html', error=error, success=success)


@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))


@app.route('/forgot-password', methods=['GET', 'POST'])
def forgot_password():
    if 'user_id' in session:
        return redirect(url_for('dashboard'))
    
    success = error = None
    if request.method == 'POST':
        email = request.form.get('email', '').strip()
        user = User.get_by_email(email)
        
        if user:
            # Create reset token
            token = User.create_reset_token(email)
            if token:
                # Send reset email
                from email_utils import send_password_reset_email
                send_password_reset_email(email, token, f"{user['first_name']} {user['last_name']}")
                success = 'Password reset link sent to your email. Please check your inbox.'
            else:
                error = 'Failed to generate reset link. Please try again.'
        else:
            # Don't reveal if email exists (security)
            success = 'If that email exists, a reset link has been sent.'
    
    return render_template('forgot_password.html', success=success, error=error)


@app.route('/reset-password/<token>', methods=['GET', 'POST'])
def reset_password(token):
    if 'user_id' in session:
        return redirect(url_for('dashboard'))
    
    # Verify token is valid
    user_id = User.verify_reset_token(token)
    if not user_id:
        return render_template('reset_password.html', error='Invalid or expired reset link.', token=None)
    
    error = success = None
    if request.method == 'POST':
        password = request.form.get('password', '')
        confirm = request.form.get('confirm_password', '')
        
        if len(password) < 6:
            error = 'Password must be at least 6 characters.'
        elif password != confirm:
            error = 'Passwords do not match.'
        else:
            if User.reset_password(token, password):
                success = 'Password reset successful! You can now login with your new password.'
                return render_template('reset_password.html', success=success, token=None)
            else:
                error = 'Failed to reset password. Please try again.'
    
    return render_template('reset_password.html', error=error, token=token)


@app.route('/profile')
def profile():
    redir = login_required()
    if redir: return redir
    user = User.get_by_id(session['user_id'])
    if not user:
        return redirect(url_for('logout'))
    return render_template('profile.html', 
                         user=user, 
                         session_name=session['user_name'],
                         role=session['role'])


@app.route('/profile/edit', methods=['GET', 'POST'])
def profile_edit():
    redir = login_required()
    if redir: return redir
    
    user = User.get_by_id(session['user_id'])
    if not user:
        return redirect(url_for('logout'))
    
    success = error = None
    if request.method == 'POST':
        first_name = request.form.get('first_name', '').strip()
        last_name = request.form.get('last_name', '').strip()
        phone = request.form.get('phone', '').strip()
        address = request.form.get('address', '').strip()
        
        if not first_name or not last_name:
            error = 'First name and last name are required.'
        else:
            User.update_profile(session['user_id'], first_name, last_name, phone, address)
            session['user_name'] = f"{first_name} {last_name}"
            
            # Send notification email
            from email_utils import send_profile_update_notification
            send_profile_update_notification(user['email'], f"{first_name} {last_name}")
            
            success = 'Profile updated successfully!'
            user = User.get_by_id(session['user_id'])  # Refresh user data
    
    return render_template('profile_edit.html', user=user, success=success, error=error,
                         session_name=session['user_name'], role=session['role'])


@app.route('/profile/change-password', methods=['POST'])
def change_password():
    redir = login_required()
    if redir: return redir
    
    current_password = request.form.get('current_password', '')
    new_password = request.form.get('new_password', '')
    confirm_password = request.form.get('confirm_password', '')
    
    user = User.get_by_id(session['user_id'])
    
    if not User.check_password(current_password, user['password_hash']):
        return redirect(url_for('profile_edit') + '?error=current')
    
    if len(new_password) < 6:
        return redirect(url_for('profile_edit') + '?error=length')
    
    if new_password != confirm_password:
        return redirect(url_for('profile_edit') + '?error=match')
    
    User.change_password(session['user_id'], new_password)
    return redirect(url_for('profile_edit') + '?success=password')


# ── Dashboard (role router) ───────────────────────────────────

@app.route('/dashboard')
def dashboard():
    redir = login_required()
    if redir: return redir
    role = session['role']
    name = session['user_name']
    if role == 'admin':
        # Get unread alerts count
        from models import _q
        alerts_result = _q("SELECT COUNT(*) as c FROM agent_notifications WHERE is_read=0", one=True)
        alerts_count = alerts_result['c'] if alerts_result else 0
        
        stats = {
            'users':    User.count(),
            'orders':   Order.count(),
            'products': Product.count(),
            'active':   Order.count_active(),
            'messages': ContactMessage.count_unread(),
            'alerts':   alerts_count,
        }
        recent = Order.get_all()[:5]
        return render_template('dashboard_admin.html', session_name=name, stats=stats, orders=recent)
    elif role == 'delivery_staff':
        active = Order.count_active()
        return render_template('dashboard_staff.html', session_name=name, active=active)
    else:
        cust = Customer.get_by_user_id(session['user_id'])
        orders = Order.get_by_customer(cust['customer_id']) if cust else []
        products = Product.get_available()[:4]  # Show 4 featured products
        total     = len(orders)
        in_del    = sum(1 for o in orders if o['order_status'] == 'out_for_delivery')
        delivered = sum(1 for o in orders if o['order_status'] == 'delivered')
        return render_template('dashboard_customer.html',
                               session_name=name, orders=orders[:5],
                               total=total, in_del=in_del, delivered=delivered,
                               products=products)


# ── Products ──────────────────────────────────────────────────

@app.route('/products')
def products():
    redir = login_required()
    if redir: return redir
    role = session['role']
    search_query = request.args.get('search', '').strip()
    page = int(request.args.get('page', 1))
    per_page = 20
    
    prods, total = Product.get_paginated(page, per_page, search_query, admin=(role == 'admin'))
    total_pages = (total + per_page - 1) // per_page
    
    return render_template('products.html', products=prods,
                           session_name=session['user_name'], role=role, 
                           search_query=search_query, page=page, total_pages=total_pages)


@app.route('/admin/product/add', methods=['POST'])
def admin_product_add():
    redir = login_required('admin')
    if redir: return redir
    Product.create(
        request.form['product_name'],
        request.form['product_category'],
        float(request.form['unit_price']),
        int(request.form['stock_quantity']),
        request.form.get('description', '')
    )
    return redirect(url_for('products'))


@app.route('/admin/product/<int:pid>/stock', methods=['POST'])
def admin_product_stock(pid):
    redir = login_required('admin')
    if redir: return redir
    qty = int(request.form['stock_quantity'])
    Product.update_stock(pid, qty)
    return redirect(url_for('products'))


@app.route('/admin/product/<int:pid>/toggle', methods=['POST'])
def admin_product_toggle(pid):
    redir = login_required('admin')
    if redir: return redir
    Product.toggle_available(pid)
    return redirect(url_for('products'))


@app.route('/admin/product/<int:pid>/price', methods=['POST'])
def admin_product_price(pid):
    redir = login_required('admin')
    if redir: return redir
    new_price = float(request.form['unit_price'])
    Product.update_price(pid, new_price)
    return redirect(url_for('products'))


@app.route('/admin/product/<int:pid>/delete', methods=['POST'])
def admin_product_delete(pid):
    redir = login_required('admin')
    if redir: return redir
    Product.delete(pid)
    return redirect(url_for('products'))


@app.route('/admin/product/<int:pid>/image', methods=['POST'])
def admin_product_image(pid):
    redir = login_required('admin')
    if redir: return redir
    
    if 'product_image' not in request.files:
        return redirect(url_for('products') + '?error=no_file')
    
    file = request.files['product_image']
    
    if file.filename == '':
        return redirect(url_for('products') + '?error=no_file')
    
    # Check file extension
    allowed_extensions = {'png', 'jpg', 'jpeg', 'gif', 'webp'}
    if '.' not in file.filename or file.filename.rsplit('.', 1)[1].lower() not in allowed_extensions:
        return redirect(url_for('products') + '?error=invalid_file')
    
    # Create safe filename
    import uuid
    from werkzeug.utils import secure_filename
    ext = file.filename.rsplit('.', 1)[1].lower()
    filename = f"product_{pid}_{uuid.uuid4().hex[:8]}.{ext}"
    
    # Ensure upload directory exists
    upload_dir = os.path.join(app.root_path, 'static', 'images', 'products')
    os.makedirs(upload_dir, exist_ok=True)
    
    # Save file
    filepath = os.path.join(upload_dir, filename)
    file.save(filepath)
    
    # Update database with relative URL
    image_url = f"/static/images/products/{filename}"
    Product.update_image(pid, image_url)
    
    return redirect(url_for('products') + '?success=image_uploaded')


@app.route('/alerts/clear', methods=['POST'])
def alerts_clear():
    redir = login_required('admin')
    if redir: return redir
    from models import _q
    _q("DELETE FROM agent_notifications", commit=True)
    return redirect(url_for('alerts'))


# ── Orders ────────────────────────────────────────────────────

@app.route('/order/new', methods=['GET', 'POST'])
def order_new():
    redir = login_required('customer')
    if redir: return redir
    prods = Product.get_available()
    preselect = int(request.args.get('product', 0))
    error = None
    if request.method == 'POST':
        cust = Customer.get_by_user_id(session['user_id'])
        if not cust:
            error = 'Customer profile not found. Please contact support.'
        else:
            items = []
            total = 0.0
            for p in prods:
                qty = int(request.form.get(f"qty_{p['product_id']}", 0))
                if qty > 0:
                    items.append((p['product_id'], qty, float(p['unit_price'])))
                    total += qty * float(p['unit_price'])
            if not items:
                error = 'Please select at least one product.'
            else:
                oid = Order.create(cust['customer_id'], total)
                for pid, qty, price in items:
                    Order.add_item(oid, pid, qty, price)
                
                # Log new order alert immediately
                log_new_order(
                    order_id=oid,
                    customer_name=session['user_name'],
                    customer_email=session.get('user_email', 'N/A'),
                    total_amount=total
                )
                
                # Send order confirmation email
                order = Order.get_by_id(oid)
                from email_utils import send_order_confirmation
                send_order_confirmation(order, session['user_email'], session['user_name'])
                
                return redirect(url_for('track_order', order_id=oid))
    return render_template('order_new.html', products=prods,
                           session_name=session['user_name'], preselect=preselect, error=error)


@app.route('/order/<int:order_id>/cancel', methods=['POST'])
def cancel_order(order_id):
    redir = login_required('customer')
    if redir: return redir
    
    order = Order.get_by_id(order_id)
    if not order:
        return redirect(url_for('my_orders'))
    
    # Check if order belongs to this customer
    cust = Customer.get_by_user_id(session['user_id'])
    if order['customer_id'] != cust['customer_id']:
        return redirect(url_for('my_orders'))
    
    # Only allow cancellation if order is pending or confirmed
    if order['order_status'] not in ['pending', 'confirmed']:
        return redirect(url_for('track_order', order_id=order_id) + '?error=cannot_cancel')
    
    reason = request.form.get('reason', 'Customer requested cancellation')
    Order.cancel_order(order_id, reason)
    
    # Send cancellation email
    from email_utils import send_order_status_update
    send_order_status_update(order, session['user_email'], session['user_name'], 
                            order['order_status'], 'cancelled')
    
    return redirect(url_for('my_orders') + '?success=cancelled')


@app.route('/my-orders')
def my_orders():
    redir = login_required('customer')
    if redir: return redir
    cust = Customer.get_by_user_id(session['user_id'])
    orders = Order.get_by_customer(cust['customer_id']) if cust else []
    return render_template('my_orders.html', orders=orders, session_name=session['user_name'])


@app.route('/track/<int:order_id>')
def track_order(order_id):
    redir = login_required()
    if redir: return redir
    order = Order.get_by_id(order_id)
    if not order:
        return render_template('404.html'), 404
    items = Order.get_items(order_id)
    return render_template('track_order.html', order=order, items=items,
                           session_name=session['user_name'], role=session['role'])


# ── Admin management ──────────────────────────────────────────

@app.route('/admin/orders/clear', methods=['POST'])
def admin_orders_clear():
    redir = login_required('admin')
    if redir: return redir
    from models import _q
    _q("DELETE FROM order_items", commit=True)
    _q("DELETE FROM orders", commit=True)
    return redirect(url_for('dashboard'))


@app.route('/admin/orders')
def admin_orders():
    redir = login_required('admin')
    if redir: return redir
    
    search_query = request.args.get('search', '').strip()
    status_filter = request.args.get('status', '').strip()
    date_from = request.args.get('date_from', '').strip()
    date_to = request.args.get('date_to', '').strip()
    page = int(request.args.get('page', 1))
    per_page = 20
    
    orders, total = Order.get_paginated(page, per_page, search_query, status_filter, date_from, date_to)
    total_pages = (total + per_page - 1) // per_page
    
    return render_template('admin_orders.html', orders=orders,
                           session_name=session['user_name'],
                           search_query=search_query,
                           status_filter=status_filter,
                           date_from=date_from,
                           date_to=date_to,
                           page=page,
                           total_pages=total_pages)


@app.route('/admin/order/<int:oid>/status', methods=['POST'])
def admin_order_status(oid):
    redir = login_required('admin')
    if redir: return redir
    
    old_order = Order.get_by_id(oid)
    old_status = old_order['order_status']
    new_status = request.form['status']
    
    Order.update_status(oid, new_status)
    
    # Send status update email
    order = Order.get_by_id(oid)
    from email_utils import send_order_status_update
    send_order_status_update(order, order['email'], 
                            f"{order['first_name']} {order['last_name']}", 
                            old_status, new_status)
    
    return redirect(url_for('admin_orders'))


@app.route('/admin/users')
def admin_users():
    redir = login_required('admin')
    if redir: return redir
    users = User.get_all()
    return render_template('admin_users.html', users=users,
                           session_name=session['user_name'])


@app.route('/admin/user/<int:uid>/toggle', methods=['POST'])
def admin_user_toggle(uid):
    redir = login_required('admin')
    if redir: return redir
    User.toggle_active(uid)
    return redirect(url_for('admin_users'))


# ── User Management ───────────────────────────────────────────

@app.route('/admin/user-management')
def admin_user_management():
    redir = login_required('admin')
    if redir: return redir
    users = User.get_all()
    success = request.args.get('success')
    error = request.args.get('error')
    return render_template('admin_user_management.html', 
                         users=users,
                         session_name=session['user_name'],
                         success=success,
                         error=error)


@app.route('/admin/user/add', methods=['POST'])
def admin_user_add():
    redir = login_required('admin')
    if redir: return redir
    
    first_name = request.form.get('first_name', '').strip()
    last_name = request.form.get('last_name', '').strip()
    email = request.form.get('email', '').strip()
    role = request.form.get('role', 'customer')
    phone = request.form.get('phone', '').strip()
    password = request.form.get('password', 'Pass@2026!')
    
    # Check if email already exists
    if User.get_by_email(email):
        return redirect(url_for('admin_user_management') + '?error=Email already exists')
    
    # Create user
    user_id = User.create(first_name, last_name, email, password, role, phone, '')
    
    # If customer, create customer profile
    if role == 'customer':
        Customer.create(user_id)
    
    return redirect(url_for('admin_user_management') + '?success=User added successfully')


@app.route('/admin/user/edit', methods=['POST'])
def admin_user_edit():
    redir = login_required('admin')
    if redir: return redir
    
    user_id = int(request.form.get('user_id'))
    first_name = request.form.get('first_name', '').strip()
    last_name = request.form.get('last_name', '').strip()
    email = request.form.get('email', '').strip()
    role = request.form.get('role', 'customer')
    phone = request.form.get('phone', '').strip()
    
    # Check if email is taken by another user
    existing = User.get_by_email(email)
    if existing and existing['user_id'] != user_id:
        return redirect(url_for('admin_user_management') + '?error=Email already taken')
    
    # Update user
    User.update_user(user_id, first_name, last_name, email, role, phone)
    
    return redirect(url_for('admin_user_management') + '?success=User updated successfully')


@app.route('/admin/user/<int:uid>/delete', methods=['POST'])
def admin_user_delete(uid):
    redir = login_required('admin')
    if redir: return redir
    
    # Don't allow deleting yourself
    if uid == session['user_id']:
        return redirect(url_for('admin_user_management') + '?error=Cannot delete your own account')
    
    User.delete_user(uid)
    return redirect(url_for('admin_user_management') + '?success=User deleted successfully')


@app.route('/admin/user/<int:uid>/reset-password', methods=['POST'])
def admin_user_reset_password(uid):
    redir = login_required('admin')
    if redir: return redir
    
    User.reset_user_password(uid, 'Pass@2026!')
    return redirect(url_for('admin_user_management') + '?success=Password reset to Pass@2026!')


# ── Public Pages ──────────────────────────────────────────────

@app.route('/developers')
def developers():
    return render_template('developers.html')


@app.route('/documentation')
def documentation():
    return render_template('documentation.html')


# ── Admin Inbox ───────────────────────────────────────────────

@app.route('/admin/inbox')
def admin_inbox():
    redir = login_required('admin')
    if redir: return redir
    
    page = int(request.args.get('page', 1))
    unread_only = request.args.get('unread', '') == '1'
    per_page = 20
    
    messages, total = ContactMessage.get_all(page, per_page, unread_only)
    total_pages = (total + per_page - 1) // per_page
    unread_count = ContactMessage.count_unread()
    
    return render_template('admin_inbox.html', 
                         messages=messages,
                         session_name=session['user_name'],
                         page=page,
                         total_pages=total_pages,
                         unread_only=unread_only,
                         unread_count=unread_count)


@app.route('/admin/inbox/<int:msg_id>')
def admin_inbox_view(msg_id):
    redir = login_required('admin')
    if redir: return redir
    
    message = ContactMessage.get_by_id(msg_id)
    if not message:
        return redirect(url_for('admin_inbox'))
    
    # Mark as read
    ContactMessage.mark_as_read(msg_id)
    
    return render_template('admin_inbox_view.html',
                         message=message,
                         session_name=session['user_name'])


@app.route('/admin/inbox/<int:msg_id>/delete', methods=['POST'])
def admin_inbox_delete(msg_id):
    redir = login_required('admin')
    if redir: return redir
    ContactMessage.delete(msg_id)
    return redirect(url_for('admin_inbox'))


# ── CSV Export ────────────────────────────────────────────────

@app.route('/admin/export/orders')
def export_orders():
    redir = login_required('admin')
    if redir: return redir
    
    # Get all orders
    orders = Order.get_all()
    
    # Create CSV
    output = StringIO()
    writer = csv.writer(output)
    
    # Write header
    writer.writerow(['Order ID', 'Customer Name', 'Email', 'Total Amount', 'Status', 'Order Date', 'Delivery Time'])
    
    # Write data
    for order in orders:
        writer.writerow([
            order['order_id'],
            f"{order['first_name']} {order['last_name']}",
            order['email'],
            f"{order['total_amount']:.2f}",
            order['order_status'],
            order['order_date'].strftime('%Y-%m-%d %H:%M:%S'),
            order['estimated_delivery_time'].strftime('%Y-%m-%d %H:%M:%S') if order['estimated_delivery_time'] else 'N/A'
        ])
    
    # Create response
    output.seek(0)
    return Response(
        output.getvalue(),
        mimetype='text/csv',
        headers={'Content-Disposition': f'attachment; filename=orders_{datetime.now().strftime("%Y%m%d_%H%M%S")}.csv'}
    )


@app.route('/admin/export/products')
def export_products():
    redir = login_required('admin')
    if redir: return redir
    
    # Get all products
    products = Product.get_all()
    
    # Create CSV
    output = StringIO()
    writer = csv.writer(output)
    
    # Write header
    writer.writerow(['Product ID', 'Name', 'Category', 'Price', 'Stock', 'Available', 'Description'])
    
    # Write data
    for product in products:
        writer.writerow([
            product['product_id'],
            product['product_name'],
            product['product_category'],
            f"{product['unit_price']:.2f}",
            product['stock_quantity'],
            'Yes' if product['is_available'] else 'No',
            product['description'] or ''
        ])
    
    # Create response
    output.seek(0)
    return Response(
        output.getvalue(),
        mimetype='text/csv',
        headers={'Content-Disposition': f'attachment; filename=products_{datetime.now().strftime("%Y%m%d_%H%M%S")}.csv'}
    )


@app.route('/admin/export/users')
def export_users():
    redir = login_required('admin')
    if redir: return redir
    
    # Get all users
    users = User.get_all()
    
    # Create CSV
    output = StringIO()
    writer = csv.writer(output)
    
    # Write header
    writer.writerow(['User ID', 'First Name', 'Last Name', 'Email', 'Role', 'Phone', 'Active', 'Created At'])
    
    # Write data
    for user in users:
        writer.writerow([
            user['user_id'],
            user['first_name'],
            user['last_name'],
            user['email'],
            user['role'],
            user['phone'] or '',
            'Yes' if user['is_active'] else 'No',
            user['created_at'].strftime('%Y-%m-%d %H:%M:%S')
        ])
    
    # Create response
    output.seek(0)
    return Response(
        output.getvalue(),
        mimetype='text/csv',
        headers={'Content-Disposition': f'attachment; filename=users_{datetime.now().strftime("%Y%m%d_%H%M%S")}.csv'}
    )



# ── Staff ─────────────────────────────────────────────────────

@app.route('/staff/deliveries')
def staff_deliveries():
    redir = login_required('delivery_staff')
    if redir: return redir
    orders = Order.get_all()
    active = [o for o in orders if o['order_status'] not in ('delivered', 'cancelled')]
    return render_template('staff_deliveries.html', orders=active,
                           session_name=session['user_name'])


@app.route('/staff/order/<int:oid>/status', methods=['POST'])
def staff_order_status(oid):
    redir = login_required('delivery_staff')
    if redir: return redir
    Order.update_status(oid, request.form['status'])
    return redirect(url_for('staff_deliveries'))


# ── Alerts ────────────────────────────────────────────────────

@app.route('/alerts')
def alerts():
    redir = login_required('admin')
    if redir: return redir
    from models import _q
    notifications = _q(
        "SELECT * FROM agent_notifications ORDER BY created_at DESC LIMIT 50"
    )
    return render_template('alerts.html', notifications=notifications)


# ── Error handlers ────────────────────────────────────────────

@app.errorhandler(400)
def bad_request(e):
    return render_template('400.html', error=str(e)), 400

@app.errorhandler(403)
def forbidden(e):
    return render_template('403.html', error=str(e)), 403

@app.errorhandler(404)
def not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(e):
    return render_template('500.html', error=str(e)), 500


# ── Entry point ───────────────────────────────────────────────

if __name__ == '__main__':
    start_agents()
    app.run(debug=True, use_reloader=False)
