"""
Script to add required users for assessment submission
Adds: admin (Pass@2026!) and basic (Pass@2026!)
"""
import bcrypt
from models import User, Customer

def add_required_users():
    """Add admin and basic users with password Pass@2026!"""
    password = "Pass@2026!"
    
    # Check if admin user exists
    admin_user = User.get_by_email('admin')
    if not admin_user:
        print("Creating admin user...")
        admin_id = User.create(
            first='Admin',
            last='User',
            email='admin',
            password=password,
            role='admin',
            phone='+675 7200 0001',
            address='Sepik Fresh HQ, Wewak'
        )
        print(f"✓ Admin user created (ID: {admin_id})")
    else:
        print("✓ Admin user already exists")
    
    # Check if basic user exists
    basic_user = User.get_by_email('basic')
    if not basic_user:
        print("Creating basic user...")
        basic_id = User.create(
            first='Basic',
            last='User',
            email='basic',
            password=password,
            role='customer',
            phone='+675 7300 0002',
            address='Wewak, East Sepik Province'
        )
        # Create customer profile for basic user
        Customer.create(basic_id)
        print(f"✓ Basic user created (ID: {basic_id})")
    else:
        print("✓ Basic user already exists")
    
    print("\n" + "="*50)
    print("Required users setup complete!")
    print("="*50)
    print("Login credentials:")
    print("  Admin: username='admin', password='Pass@2026!'")
    print("  Basic: username='basic', password='Pass@2026!'")
    print("="*50)

if __name__ == '__main__':
    add_required_users()
