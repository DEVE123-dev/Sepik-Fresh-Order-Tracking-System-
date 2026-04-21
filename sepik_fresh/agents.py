"""
agents.py — Background Agents for Sepik Fresh Tracking System

Three agents run as daemon threads alongside the Flask app:

  1. OrderStatusAgent   — Detects order status changes and logs notifications
  2. StockAlertAgent    — Alerts admin when product stock falls below threshold
  3. DeliveryCheckAgent — Flags overdue deliveries that missed their ETA

Each agent runs in an infinite loop with a sleep interval between checks.
They are started once when app.py launches and stop when the app stops.
"""

import threading
import time
import mysql.connector
from datetime import datetime
from config import Config

# ── Database config (from centralized config) ──
def get_db():
    """Opens a MySQL connection for agent use."""
    return mysql.connector.connect(**Config.get_db_config())

# ── Low stock threshold ──
STOCK_THRESHOLD = 10

# ── How often each agent checks (seconds) ──
ORDER_CHECK_INTERVAL   = 30   # every 30 seconds
STOCK_CHECK_INTERVAL   = 60   # every 60 seconds
DELIVERY_CHECK_INTERVAL = 60  # every 60 seconds


# ─────────────────────────────────────────────────────────────
# AGENT 1: ORDER STATUS AGENT
# Watches the orders table for status changes.
# When a status changes, it logs a notification entry.
# In a real system this would send an SMS or email.
# ─────────────────────────────────────────────────────────────

# Tracks the last known status of each order {order_id: status}
_order_status_cache = {}

def order_status_agent():
    """
    Runs every 30 seconds.
    Compares current order statuses against a cached snapshot.
    If a status has changed, logs a notification.
    """
    print("[Agent] OrderStatusAgent started.")
    # Give the app a moment to fully start before first check
    time.sleep(5)

    while True:
        try:
            conn   = get_db()
            cursor = conn.cursor(dictionary=True)
            cursor.execute(
                "SELECT o.order_id, o.order_status, "
                "u.first_name, u.last_name, u.email "
                "FROM orders o "
                "JOIN customers c ON o.customer_id = c.customer_id "
                "JOIN users u ON c.user_id = u.user_id"
            )
            orders = cursor.fetchall()
            cursor.close()
            conn.close()

            for order in orders:
                oid    = order['order_id']
                status = order['order_status']
                name   = f"{order['first_name']} {order['last_name']}"
                email  = order['email']

                if oid not in _order_status_cache:
                    # First time seeing this order — just cache it
                    _order_status_cache[oid] = status
                elif _order_status_cache[oid] != status:
                    # Status has changed — log the notification
                    old = _order_status_cache[oid]
                    _order_status_cache[oid] = status
                    _log_notification(
                        agent   = 'OrderStatusAgent',
                        message = (
                            f"Order #{oid} for {name} ({email}) "
                            f"changed from '{old}' to '{status}'."
                        )
                    )

        except Exception as e:
            print(f"[OrderStatusAgent] Error: {e}")

        time.sleep(ORDER_CHECK_INTERVAL)


# ─────────────────────────────────────────────────────────────
# AGENT 2: STOCK ALERT AGENT
# Checks product stock levels every 60 seconds.
# Logs an alert when any product falls below STOCK_THRESHOLD.
# ─────────────────────────────────────────────────────────────

# Tracks which products have already been alerted {product_id: True}
_stock_alerted = {}

def stock_alert_agent():
    """
    Runs every 60 seconds.
    Queries all products and checks stock_quantity.
    Logs an alert if stock is below the threshold.
    Resets the alert once stock is restocked above threshold.
    """
    print("[Agent] StockAlertAgent started.")
    time.sleep(8)

    while True:
        try:
            conn   = get_db()
            cursor = conn.cursor(dictionary=True)
            cursor.execute(
                "SELECT product_id, product_name, stock_quantity "
                "FROM products WHERE is_available = 1"
            )
            products = cursor.fetchall()
            cursor.close()
            conn.close()

            for product in products:
                pid   = product['product_id']
                name  = product['product_name']
                stock = product['stock_quantity']

                if stock < STOCK_THRESHOLD and not _stock_alerted.get(pid):
                    _stock_alerted[pid] = True
                    _log_notification(
                        agent   = 'StockAlertAgent',
                        message = (
                            f"LOW STOCK: '{name}' has only {stock} units left. "
                            f"Admin action required."
                        )
                    )
                elif stock >= STOCK_THRESHOLD and _stock_alerted.get(pid):
                    # Stock has been restocked — reset the alert
                    _stock_alerted[pid] = False
                    _log_notification(
                        agent   = 'StockAlertAgent',
                        message = (
                            f"RESTOCKED: '{name}' is back to {stock} units."
                        )
                    )

        except Exception as e:
            print(f"[StockAlertAgent] Error: {e}")

        time.sleep(STOCK_CHECK_INTERVAL)


# ─────────────────────────────────────────────────────────────
# AGENT 3: DELIVERY CHECK AGENT
# Checks every 60 seconds for orders that have passed their
# estimated_delivery_time but are still not marked 'delivered'.
# ─────────────────────────────────────────────────────────────

# Tracks which overdue orders have already been flagged
_overdue_alerted = set()

def delivery_check_agent():
    """
    Runs every 60 seconds.
    Finds orders where estimated_delivery_time has passed
    but order_status is not 'delivered' or 'cancelled'.
    Logs a delay alert for each overdue order.
    """
    print("[Agent] DeliveryCheckAgent started.")
    time.sleep(10)

    while True:
        try:
            conn   = get_db()
            cursor = conn.cursor(dictionary=True)
            cursor.execute(
                "SELECT o.order_id, o.order_status, o.estimated_delivery_time, "
                "u.first_name, u.last_name, u.email "
                "FROM orders o "
                "JOIN customers c ON o.customer_id = c.customer_id "
                "JOIN users u ON c.user_id = u.user_id "
                "WHERE o.estimated_delivery_time IS NOT NULL "
                "AND o.order_status NOT IN ('delivered', 'cancelled')"
            )
            orders = cursor.fetchall()
            cursor.close()
            conn.close()

            now = datetime.now()

            for order in orders:
                oid = order['order_id']
                eta = order['estimated_delivery_time']
                name  = f"{order['first_name']} {order['last_name']}"
                email = order['email']

                # eta comes back as a datetime object from MySQL
                if isinstance(eta, datetime) and now > eta and oid not in _overdue_alerted:
                    _overdue_alerted.add(oid)
                    overdue_mins = int((now - eta).total_seconds() / 60)
                    _log_notification(
                        agent   = 'DeliveryCheckAgent',
                        message = (
                            f"OVERDUE: Order #{oid} for {name} ({email}) "
                            f"is {overdue_mins} minute(s) past its ETA "
                            f"({eta.strftime('%Y-%m-%d %H:%M')}). "
                            f"Status: {order['order_status']}."
                        )
                    )

        except Exception as e:
            print(f"[DeliveryCheckAgent] Error: {e}")

        time.sleep(DELIVERY_CHECK_INTERVAL)


# ─────────────────────────────────────────────────────────────
# NOTIFICATION LOGGER
# Writes agent alerts to the agent_notifications table in MySQL
# and also prints them to the terminal.
# ─────────────────────────────────────────────────────────────

def _log_notification(agent: str, message: str):
    """
    Saves a notification to the database and prints it to terminal.
    The admin dashboard can query this table to display alerts.
    """
    print(f"[{agent}] {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} — {message}")
    try:
        conn   = get_db()
        cursor = conn.cursor(dictionary=True)
        cursor.execute(
            "INSERT INTO agent_notifications (agent_name, message) VALUES (%s, %s)",
            (agent, message)
        )
        conn.commit()
        cursor.close()
        conn.close()
    except Exception as e:
        print(f"[_log_notification] Could not save to DB: {e}")


# ─────────────────────────────────────────────────────────────
# NEW ORDER NOTIFICATION (called directly from app.py)
# This function is called immediately when a customer places an order
# ─────────────────────────────────────────────────────────────

def log_new_order(order_id: int, customer_name: str, customer_email: str, total_amount: float):
    """
    Called immediately when a new order is placed.
    Logs an instant notification for admin to see.
    """
    _log_notification(
        agent   = 'NewOrderAlert',
        message = (
            f"NEW ORDER PLACED: Order #{order_id} by {customer_name} ({customer_email}) "
            f"for K{total_amount:.2f}. Awaiting confirmation."
        )
    )


# ─────────────────────────────────────────────────────────────
# START ALL AGENTS
# Called once from app.py on startup.
# Each agent runs as a daemon thread — it stops automatically
# when the main Flask process stops.
# ─────────────────────────────────────────────────────────────

def start_agents():
    """Starts all three agents as background daemon threads."""
    agents = [
        threading.Thread(target=order_status_agent,   name='OrderStatusAgent',   daemon=True),
        threading.Thread(target=stock_alert_agent,    name='StockAlertAgent',    daemon=True),
        threading.Thread(target=delivery_check_agent, name='DeliveryCheckAgent', daemon=True),
    ]
    for agent in agents:
        agent.start()
    print("[Agents] All agents running.")
