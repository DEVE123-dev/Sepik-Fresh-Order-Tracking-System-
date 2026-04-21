"""
models.py — OOP Model Classes for Sepik Fresh
Each class represents a database table and encapsulates all SQL for that entity.
"""
import bcrypt
import mysql.connector
from config import Config

def get_db():
    return mysql.connector.connect(**Config.get_db_config())

def _q(sql, params=(), one=False, commit=False):
    """Universal query helper. Returns dict rows."""
    conn = get_db()
    cur  = conn.cursor(dictionary=True)
    cur.execute(sql, params)
    if commit:
        conn.commit()
        result = cur.lastrowid
    elif one:
        result = cur.fetchone()
    else:
        result = cur.fetchall()
    cur.close(); conn.close()
    return result


class User:
    @staticmethod
    def get_by_email(email):
        return _q("SELECT * FROM users WHERE email=%s AND is_active=1", (email,), one=True)

    @staticmethod
    def get_by_id(uid):
        return _q("SELECT * FROM users WHERE user_id=%s", (uid,), one=True)

    @staticmethod
    def get_all():
        return _q("SELECT user_id,first_name,last_name,email,role,phone,is_active,created_at FROM users ORDER BY created_at DESC")

    @staticmethod
    def create(first, last, email, password, role, phone='', address=''):
        hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
        return _q(
            "INSERT INTO users (first_name,last_name,email,password_hash,role,phone,address) VALUES (%s,%s,%s,%s,%s,%s,%s)",
            (first, last, email, hashed, role, phone, address), commit=True
        )

    @staticmethod
    def toggle_active(uid):
        _q("UPDATE users SET is_active = NOT is_active WHERE user_id=%s", (uid,), commit=True)

    @staticmethod
    def check_password(plain, stored_hash):
        try:
            return bcrypt.checkpw(plain.encode(), stored_hash.encode())
        except ValueError:
            return False

    @staticmethod
    def count():
        r = _q("SELECT COUNT(*) as c FROM users", one=True)
        return r['c'] if r else 0

    @staticmethod
    def create_reset_token(email):
        """Create password reset token for user"""
        import secrets
        from datetime import datetime, timedelta
        
        user = User.get_by_email(email)
        if not user:
            return None
        
        # Generate secure token
        token = secrets.token_urlsafe(32)
        expires_at = datetime.now() + timedelta(hours=1)
        
        # Save token to database
        _q(
            "INSERT INTO password_reset_tokens (user_id, token, expires_at) VALUES (%s, %s, %s)",
            (user['user_id'], token, expires_at),
            commit=True
        )
        
        return token
    
    @staticmethod
    def verify_reset_token(token):
        """Verify password reset token and return user_id if valid"""
        from datetime import datetime
        
        result = _q(
            "SELECT user_id, expires_at FROM password_reset_tokens "
            "WHERE token=%s AND used=0",
            (token,),
            one=True
        )
        
        if not result:
            return None
        
        # Check if expired
        if datetime.now() > result['expires_at']:
            return None
        
        return result['user_id']
    
    @staticmethod
    def reset_password(token, new_password):
        """Reset password using token"""
        user_id = User.verify_reset_token(token)
        if not user_id:
            return False
        
        # Hash new password
        hashed = bcrypt.hashpw(new_password.encode(), bcrypt.gensalt()).decode()
        
        # Update password
        _q("UPDATE users SET password_hash=%s WHERE user_id=%s", (hashed, user_id), commit=True)
        
        # Mark token as used
        _q("UPDATE password_reset_tokens SET used=1 WHERE token=%s", (token,), commit=True)
        
        return True
    
    @staticmethod
    def update_profile(user_id, first_name, last_name, phone, address):
        """Update user profile information"""
        _q(
            "UPDATE users SET first_name=%s, last_name=%s, phone=%s, address=%s WHERE user_id=%s",
            (first_name, last_name, phone, address, user_id),
            commit=True
        )
    
    @staticmethod
    def change_password(user_id, new_password):
        """Change user password"""
        hashed = bcrypt.hashpw(new_password.encode(), bcrypt.gensalt()).decode()
        _q("UPDATE users SET password_hash=%s WHERE user_id=%s", (hashed, user_id), commit=True)
    
    @staticmethod
    def update_user(user_id, first_name, last_name, email, role, phone):
        """Update user details (admin function)"""
        _q(
            "UPDATE users SET first_name=%s, last_name=%s, email=%s, role=%s, phone=%s WHERE user_id=%s",
            (first_name, last_name, email, role, phone, user_id),
            commit=True
        )
    
    @staticmethod
    def delete_user(user_id):
        """Delete a user (admin function)"""
        # First delete customer profile if exists
        _q("DELETE FROM customers WHERE user_id=%s", (user_id,), commit=True)
        # Then delete user
        _q("DELETE FROM users WHERE user_id=%s", (user_id,), commit=True)
    
    @staticmethod
    def reset_user_password(user_id, new_password):
        """Reset user password to default (admin function)"""
        hashed = bcrypt.hashpw(new_password.encode(), bcrypt.gensalt()).decode()
        _q("UPDATE users SET password_hash=%s WHERE user_id=%s", (hashed, user_id), commit=True)


class Product:
    @staticmethod
    def get_all():
        return _q("SELECT * FROM products ORDER BY created_at DESC")

    @staticmethod
    def get_available():
        return _q("SELECT * FROM products WHERE is_available=1 ORDER BY product_name")

    @staticmethod
    def get_by_id(pid):
        return _q("SELECT * FROM products WHERE product_id=%s", (pid,), one=True)

    @staticmethod
    def search(query):
        """Search products by name or description"""
        search_term = f"%{query}%"
        return _q(
            "SELECT * FROM products WHERE (product_name LIKE %s OR description LIKE %s) AND is_available=1 ORDER BY product_name",
            (search_term, search_term)
        )

    @staticmethod
    def create(name, category, price, stock, description='', image_url=''):
        return _q(
            "INSERT INTO products (product_name,product_category,unit_price,stock_quantity,description,image_url) VALUES (%s,%s,%s,%s,%s,%s)",
            (name, category, price, stock, description, image_url), commit=True
        )

    @staticmethod
    def update_stock(pid, qty):
        _q("UPDATE products SET stock_quantity=%s WHERE product_id=%s", (qty, pid), commit=True)

    @staticmethod
    def update_price(pid, price):
        _q("UPDATE products SET unit_price=%s WHERE product_id=%s", (price, pid), commit=True)
    
    @staticmethod
    def update_image(pid, image_url):
        _q("UPDATE products SET image_url=%s WHERE product_id=%s", (image_url, pid), commit=True)

    @staticmethod
    def toggle_available(pid):
        _q("UPDATE products SET is_available = NOT is_available WHERE product_id=%s", (pid,), commit=True)

    @staticmethod
    def delete(pid):
        # First check if product is used in any orders
        check = _q("SELECT COUNT(*) as c FROM order_items WHERE product_id=%s", (pid,), one=True)
        if check and check['c'] > 0:
            # If product has orders, just disable it instead of deleting
            _q("UPDATE products SET is_available=0 WHERE product_id=%s", (pid,), commit=True)
        else:
            # If no orders, safe to delete
            _q("DELETE FROM products WHERE product_id=%s", (pid,), commit=True)

    @staticmethod
    def count():
        r = _q("SELECT COUNT(*) as c FROM products WHERE is_available=1", one=True)
        return r['c'] if r else 0
    
    @staticmethod
    def get_paginated(page=1, per_page=20, search_query='', admin=False):
        """Get paginated products with search"""
        offset = (page - 1) * per_page
        
        if search_query:
            search_term = f"%{search_query}%"
            if admin:
                products = _q(
                    "SELECT * FROM products WHERE product_name LIKE %s OR description LIKE %s "
                    "ORDER BY created_at DESC LIMIT %s OFFSET %s",
                    (search_term, search_term, per_page, offset)
                )
                total = _q(
                    "SELECT COUNT(*) as c FROM products WHERE product_name LIKE %s OR description LIKE %s",
                    (search_term, search_term), one=True
                )['c']
            else:
                products = _q(
                    "SELECT * FROM products WHERE (product_name LIKE %s OR description LIKE %s) AND is_available=1 "
                    "ORDER BY product_name LIMIT %s OFFSET %s",
                    (search_term, search_term, per_page, offset)
                )
                total = _q(
                    "SELECT COUNT(*) as c FROM products WHERE (product_name LIKE %s OR description LIKE %s) AND is_available=1",
                    (search_term, search_term), one=True
                )['c']
        else:
            if admin:
                products = _q("SELECT * FROM products ORDER BY created_at DESC LIMIT %s OFFSET %s", (per_page, offset))
                total = _q("SELECT COUNT(*) as c FROM products", one=True)['c']
            else:
                products = _q("SELECT * FROM products WHERE is_available=1 ORDER BY product_name LIMIT %s OFFSET %s", (per_page, offset))
                total = _q("SELECT COUNT(*) as c FROM products WHERE is_available=1", one=True)['c']
        
        return products, total


class Order:
    @staticmethod
    def get_all():
        return _q(
            "SELECT o.*, u.first_name, u.last_name, u.email "
            "FROM orders o JOIN customers c ON o.customer_id=c.customer_id "
            "JOIN users u ON c.user_id=u.user_id ORDER BY o.created_at DESC"
        )

    @staticmethod
    def search(query):
        """Search orders by ID, customer name, or email"""
        search_term = f"%{query}%"
        return _q(
            "SELECT o.*, u.first_name, u.last_name, u.email "
            "FROM orders o JOIN customers c ON o.customer_id=c.customer_id "
            "JOIN users u ON c.user_id=u.user_id "
            "WHERE o.order_id LIKE %s OR u.first_name LIKE %s OR u.last_name LIKE %s OR u.email LIKE %s "
            "ORDER BY o.created_at DESC",
            (search_term, search_term, search_term, search_term)
        )

    @staticmethod
    def filter_by_status(status):
        """Filter orders by status"""
        return _q(
            "SELECT o.*, u.first_name, u.last_name, u.email "
            "FROM orders o JOIN customers c ON o.customer_id=c.customer_id "
            "JOIN users u ON c.user_id=u.user_id "
            "WHERE o.order_status=%s ORDER BY o.created_at DESC",
            (status,)
        )

    @staticmethod
    def get_by_id(oid):
        return _q(
            "SELECT o.*, u.first_name, u.last_name, u.email, u.phone, u.address "
            "FROM orders o JOIN customers c ON o.customer_id=c.customer_id "
            "JOIN users u ON c.user_id=u.user_id WHERE o.order_id=%s", (oid,), one=True
        )

    @staticmethod
    def get_by_customer(customer_id):
        return _q(
            "SELECT * FROM orders WHERE customer_id=%s ORDER BY created_at DESC",
            (customer_id,)
        )

    @staticmethod
    def get_items(oid):
        return _q(
            "SELECT oi.*, p.product_name, p.unit_price "
            "FROM order_items oi JOIN products p ON oi.product_id=p.product_id "
            "WHERE oi.order_id=%s", (oid,)
        )

    @staticmethod
    def create(customer_id, total, eta=None):
        return _q(
            "INSERT INTO orders (customer_id, total_amount, estimated_delivery_time) VALUES (%s,%s,%s)",
            (customer_id, total, eta), commit=True
        )

    @staticmethod
    def add_item(order_id, product_id, qty, price):
        _q(
            "INSERT INTO order_items (order_id,product_id,quantity,unit_price) VALUES (%s,%s,%s,%s)",
            (order_id, product_id, qty, price), commit=True
        )
        # Deduct stock
        _q("UPDATE products SET stock_quantity = stock_quantity - %s WHERE product_id=%s",
           (qty, product_id), commit=True)

    @staticmethod
    def update_status(oid, status):
        _q("UPDATE orders SET order_status=%s WHERE order_id=%s", (status, oid), commit=True)

    @staticmethod
    def count():
        r = _q("SELECT COUNT(*) as c FROM orders", one=True)
        return r['c'] if r else 0

    @staticmethod
    def count_active():
        r = _q("SELECT COUNT(*) as c FROM orders WHERE order_status NOT IN ('delivered','cancelled')", one=True)
        return r['c'] if r else 0
    
    @staticmethod
    def get_paginated(page=1, per_page=20, search_query='', status_filter='', date_from='', date_to=''):
        """Get paginated orders with search and filters"""
        offset = (page - 1) * per_page
        
        # Build WHERE clause
        where_clauses = []
        params = []
        
        if search_query:
            search_term = f"%{search_query}%"
            where_clauses.append("(o.order_id LIKE %s OR u.first_name LIKE %s OR u.last_name LIKE %s OR u.email LIKE %s)")
            params.extend([search_term, search_term, search_term, search_term])
        
        if status_filter:
            where_clauses.append("o.order_status = %s")
            params.append(status_filter)
        
        if date_from:
            where_clauses.append("DATE(o.created_at) >= %s")
            params.append(date_from)
        
        if date_to:
            where_clauses.append("DATE(o.created_at) <= %s")
            params.append(date_to)
        
        where_sql = " AND ".join(where_clauses) if where_clauses else "1=1"
        
        # Get orders
        orders = _q(
            f"SELECT o.*, u.first_name, u.last_name, u.email "
            f"FROM orders o JOIN customers c ON o.customer_id=c.customer_id "
            f"JOIN users u ON c.user_id=u.user_id "
            f"WHERE {where_sql} ORDER BY o.created_at DESC LIMIT %s OFFSET %s",
            tuple(params + [per_page, offset])
        )
        
        # Get total count
        total = _q(
            f"SELECT COUNT(*) as c FROM orders o "
            f"JOIN customers c ON o.customer_id=c.customer_id "
            f"JOIN users u ON c.user_id=u.user_id WHERE {where_sql}",
            tuple(params), one=True
        )['c']
        
        return orders, total

    @staticmethod
    def cancel_order(order_id, reason=''):
        """Cancel an order and restore stock"""
        from datetime import datetime
        
        # Get order items to restore stock
        items = Order.get_items(order_id)
        
        # Restore stock for each item
        for item in items:
            _q(
                "UPDATE products SET stock_quantity = stock_quantity + %s WHERE product_id=%s",
                (item['quantity'], item['product_id']),
                commit=True
            )
        
        # Update order status
        _q(
            "UPDATE orders SET order_status='cancelled', cancelled_at=%s, cancellation_reason=%s WHERE order_id=%s",
            (datetime.now(), reason, order_id),
            commit=True
        )


class Customer:
    @staticmethod
    def get_by_user_id(uid):
        return _q("SELECT * FROM customers WHERE user_id=%s", (uid,), one=True)

    @staticmethod
    def create(uid):
        # Generate customer number
        r = _q("SELECT COUNT(*) as c FROM customers", one=True)
        num = f"SF-CUST-{(r['c']+1):05d}"
        return _q(
            "INSERT INTO customers (user_id, customer_number) VALUES (%s,%s)",
            (uid, num), commit=True
        )


class ContactMessage:
    @staticmethod
    def get_all(page=1, per_page=20, unread_only=False):
        """Get paginated contact messages"""
        offset = (page - 1) * per_page
        
        where_sql = "WHERE is_read=0" if unread_only else ""
        
        messages = _q(
            f"SELECT * FROM contact_messages {where_sql} ORDER BY created_at DESC LIMIT %s OFFSET %s",
            (per_page, offset)
        )
        
        total = _q(f"SELECT COUNT(*) as c FROM contact_messages {where_sql}", one=True)['c']
        
        return messages, total
    
    @staticmethod
    def get_by_id(msg_id):
        return _q("SELECT * FROM contact_messages WHERE id=%s", (msg_id,), one=True)
    
    @staticmethod
    def mark_as_read(msg_id):
        _q("UPDATE contact_messages SET is_read=1 WHERE id=%s", (msg_id,), commit=True)
    
    @staticmethod
    def delete(msg_id):
        _q("DELETE FROM contact_messages WHERE id=%s", (msg_id,), commit=True)
    
    @staticmethod
    def count_unread():
        r = _q("SELECT COUNT(*) as c FROM contact_messages WHERE is_read=0", one=True)
        return r['c'] if r else 0
