"""
setup.py — Sepik Fresh First-Time Setup Script

Run this ONCE before starting the app for the first time.
It automatically creates the database and imports all tables and data.

Usage:
    python setup.py

Requirements:
    - XAMPP must be running (Apache + MySQL started)
    - Python packages installed:
        python -m pip install flask mysql-connector-python bcrypt
"""

import mysql.connector
import os

# MySQL connection — default XAMPP settings
HOST     = '127.0.0.1'
USER     = 'root'
PASSWORD = ''  # XAMPP default is no password

SQL_FILE = os.path.join(os.path.dirname(__file__), 'database', 'sepik_database.sql')

def run_setup():
    print("=" * 50)
    print("  Sepik Fresh — Database Setup")
    print("=" * 50)

    try:
        # Connect without specifying a database first
        conn   = mysql.connector.connect(host=HOST, user=USER, password=PASSWORD)
        cursor = conn.cursor()

        # Read the SQL file
        with open(SQL_FILE, 'r', encoding='utf-8') as f:
            sql = f.read()

        # Split into individual statements and run each one
        statements = [s.strip() for s in sql.split(';') if s.strip()]
        for statement in statements:
            try:
                cursor.execute(statement)
            except mysql.connector.Error as e:
                # Skip warnings like "table already exists"
                if e.errno in (1007, 1050, 1062):
                    pass  # Database/table already exists or duplicate entry
                else:
                    print(f"  Warning: {e}")

        conn.commit()
        cursor.close()
        conn.close()

        print("\n  Database setup complete.")
        print("  You can now run the app with:  python app.py")
        print("  Then open:  http://127.0.0.1:5000\n")

    except mysql.connector.Error as e:
        print(f"\n  ERROR: Could not connect to MySQL.")
        print(f"  Make sure XAMPP is running and MySQL is started.")
        print(f"  Details: {e}\n")

if __name__ == '__main__':
    run_setup()
