"""
email_utils.py — Email Notification System for Sepik Fresh
Handles sending emails for order confirmations, password resets, etc.
"""
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from config import Config
from datetime import datetime

def log_email(email, subject, message, email_type, user_id=None):
    """Log email to database for tracking"""
    from models import _q
    try:
        _q(
            "INSERT INTO email_notifications (user_id, email, subject, message, type, sent, sent_at) "
            "VALUES (%s, %s, %s, %s, %s, %s, %s)",
            (user_id, email, subject, message, email_type, 1, datetime.now()),
            commit=True
        )
    except Exception as e:
        print(f"[Email Log Error] {e}")


def send_email(to_email, subject, html_content, email_type='general', user_id=None):
    """
    Send email using SMTP
    Returns True if successful, False otherwise
    """
    # If email is not configured, just log it
    if not Config.MAIL_USERNAME or not Config.MAIL_PASSWORD:
        print(f"[Email] Would send to {to_email}: {subject}")
        log_email(to_email, subject, html_content, email_type, user_id)
        return True
    
    try:
        # Create message
        msg = MIMEMultipart('alternative')
        msg['From'] = Config.MAIL_DEFAULT_SENDER
        msg['To'] = to_email
        msg['Subject'] = subject
        
        # Attach HTML content
        html_part = MIMEText(html_content, 'html')
        msg.attach(html_part)
        
        # Send email
        with smtplib.SMTP(Config.MAIL_SERVER, Config.MAIL_PORT) as server:
            server.starttls()
            server.login(Config.MAIL_USERNAME, Config.MAIL_PASSWORD)
            server.send_message(msg)
        
        # Log success
        log_email(to_email, subject, html_content, email_type, user_id)
        print(f"[Email] Sent to {to_email}: {subject}")
        return True
        
    except Exception as e:
        print(f"[Email Error] {e}")
        # Log failed attempt
        log_email(to_email, subject, html_content, email_type, user_id)
        return False


def send_order_confirmation(order, customer_email, customer_name):
    """Send order confirmation email"""
    subject = f"Order Confirmation - #{order['order_id']}"
    
    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <style>
            body {{ font-family: Arial, sans-serif; line-height: 1.6; color: #333; }}
            .container {{ max-width: 600px; margin: 0 auto; padding: 20px; }}
            .header {{ background: #2a7a30; color: white; padding: 20px; text-align: center; }}
            .content {{ padding: 20px; background: #f9f9f9; }}
            .order-details {{ background: white; padding: 15px; margin: 15px 0; border-radius: 5px; }}
            .footer {{ text-align: center; padding: 20px; color: #666; font-size: 12px; }}
            .button {{ display: inline-block; padding: 12px 24px; background: #2a7a30; color: white; text-decoration: none; border-radius: 5px; margin: 10px 0; }}
        </style>
    </head>
    <body>
        <div class="container">
            <div class="header">
                <h1>Sepik Fresh</h1>
                <p>Order Confirmation</p>
            </div>
            <div class="content">
                <h2>Thank you for your order, {customer_name}!</h2>
                <p>Your order has been received and is being processed.</p>
                
                <div class="order-details">
                    <h3>Order Details</h3>
                    <p><strong>Order ID:</strong> #{order['order_id']}</p>
                    <p><strong>Total Amount:</strong> K{order['total_amount']:.2f}</p>
                    <p><strong>Status:</strong> {order['order_status'].replace('_', ' ').title()}</p>
                    <p><strong>Order Date:</strong> {order['order_date'].strftime('%d %B %Y')}</p>
                </div>
                
                <p>You can track your order status anytime by logging into your account.</p>
                
                <a href="http://localhost:5000/track/{order['order_id']}" class="button">Track Order</a>
                
                <p>If you have any questions, please contact us at info@sepikfresh.pg</p>
            </div>
            <div class="footer">
                <p>&copy; 2026 Sepik Fresh. All rights reserved.</p>
                <p>Wewak, East Sepik Province, PNG</p>
            </div>
        </div>
    </body>
    </html>
    """
    
    return send_email(customer_email, subject, html_content, 'order_confirmation', order.get('customer_id'))


def send_order_status_update(order, customer_email, customer_name, old_status, new_status):
    """Send order status update email"""
    subject = f"Order Update - #{order['order_id']}"
    
    status_messages = {
        'confirmed': 'Your order has been confirmed and is being prepared.',
        'processing': 'Your order is being processed.',
        'out_for_delivery': 'Your order is out for delivery!',
        'delivered': 'Your order has been delivered. Thank you for choosing Sepik Fresh!',
        'cancelled': 'Your order has been cancelled.'
    }
    
    message = status_messages.get(new_status, 'Your order status has been updated.')
    
    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <style>
            body {{ font-family: Arial, sans-serif; line-height: 1.6; color: #333; }}
            .container {{ max-width: 600px; margin: 0 auto; padding: 20px; }}
            .header {{ background: #2a7a30; color: white; padding: 20px; text-align: center; }}
            .content {{ padding: 20px; background: #f9f9f9; }}
            .status-update {{ background: white; padding: 15px; margin: 15px 0; border-radius: 5px; border-left: 4px solid #2a7a30; }}
            .footer {{ text-align: center; padding: 20px; color: #666; font-size: 12px; }}
            .button {{ display: inline-block; padding: 12px 24px; background: #2a7a30; color: white; text-decoration: none; border-radius: 5px; margin: 10px 0; }}
        </style>
    </head>
    <body>
        <div class="container">
            <div class="header">
                <h1>Sepik Fresh</h1>
                <p>Order Status Update</p>
            </div>
            <div class="content">
                <h2>Hello {customer_name},</h2>
                
                <div class="status-update">
                    <h3>Order #{order['order_id']}</h3>
                    <p><strong>Status:</strong> {new_status.replace('_', ' ').title()}</p>
                    <p>{message}</p>
                </div>
                
                <a href="http://localhost:5000/track/{order['order_id']}" class="button">Track Order</a>
            </div>
            <div class="footer">
                <p>&copy; 2026 Sepik Fresh. All rights reserved.</p>
            </div>
        </div>
    </body>
    </html>
    """
    
    return send_email(customer_email, subject, html_content, 'status_update', order.get('customer_id'))


def send_password_reset_email(email, reset_token, user_name):
    """Send password reset email"""
    subject = "Password Reset Request - Sepik Fresh"
    reset_link = f"http://localhost:5000/reset-password/{reset_token}"
    
    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <style>
            body {{ font-family: Arial, sans-serif; line-height: 1.6; color: #333; }}
            .container {{ max-width: 600px; margin: 0 auto; padding: 20px; }}
            .header {{ background: #2a7a30; color: white; padding: 20px; text-align: center; }}
            .content {{ padding: 20px; background: #f9f9f9; }}
            .reset-box {{ background: white; padding: 20px; margin: 15px 0; border-radius: 5px; text-align: center; }}
            .button {{ display: inline-block; padding: 12px 24px; background: #2a7a30; color: white; text-decoration: none; border-radius: 5px; margin: 10px 0; }}
            .warning {{ background: #fff3cd; padding: 10px; border-radius: 5px; margin: 10px 0; }}
            .footer {{ text-align: center; padding: 20px; color: #666; font-size: 12px; }}
        </style>
    </head>
    <body>
        <div class="container">
            <div class="header">
                <h1>Sepik Fresh</h1>
                <p>Password Reset Request</p>
            </div>
            <div class="content">
                <h2>Hello {user_name},</h2>
                <p>We received a request to reset your password. Click the button below to create a new password:</p>
                
                <div class="reset-box">
                    <a href="{reset_link}" class="button">Reset Password</a>
                    <p style="margin-top: 15px; font-size: 12px; color: #666;">
                        Or copy this link: <br>
                        <code style="background: #f0f0f0; padding: 5px; display: inline-block; margin-top: 5px;">{reset_link}</code>
                    </p>
                </div>
                
                <div class="warning">
                    <strong>⚠️ Important:</strong>
                    <ul style="margin: 5px 0; padding-left: 20px;">
                        <li>This link expires in 1 hour</li>
                        <li>If you didn't request this, please ignore this email</li>
                        <li>Your password won't change until you create a new one</li>
                    </ul>
                </div>
            </div>
            <div class="footer">
                <p>&copy; 2026 Sepik Fresh. All rights reserved.</p>
            </div>
        </div>
    </body>
    </html>
    """
    
    return send_email(email, subject, html_content, 'password_reset')


def send_profile_update_notification(email, user_name):
    """Send notification when profile is updated"""
    subject = "Profile Updated - Sepik Fresh"
    
    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <style>
            body {{ font-family: Arial, sans-serif; line-height: 1.6; color: #333; }}
            .container {{ max-width: 600px; margin: 0 auto; padding: 20px; }}
            .header {{ background: #2a7a30; color: white; padding: 20px; text-align: center; }}
            .content {{ padding: 20px; background: #f9f9f9; }}
            .footer {{ text-align: center; padding: 20px; color: #666; font-size: 12px; }}
        </style>
    </head>
    <body>
        <div class="container">
            <div class="header">
                <h1>Sepik Fresh</h1>
            </div>
            <div class="content">
                <h2>Hello {user_name},</h2>
                <p>Your profile information has been successfully updated.</p>
                <p>If you didn't make this change, please contact us immediately at info@sepikfresh.pg</p>
            </div>
            <div class="footer">
                <p>&copy; 2026 Sepik Fresh. All rights reserved.</p>
            </div>
        </div>
    </body>
    </html>
    """
    
    return send_email(email, subject, html_content, 'profile_update')
