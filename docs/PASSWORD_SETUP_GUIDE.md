# Password Setup Guide

## Important: How Passwords Work in This Project

### Why Passwords Are Not in database.sql

The `database.sql` file does **NOT** include the admin and basic users with pre-hashed passwords. This is intentional and follows security best practices:

1. **Security**: Bcrypt generates unique salts for each password hash
2. **Freshness**: Each installation gets newly generated hashes
3. **Best Practice**: Passwords should be hashed at runtime, not stored in SQL files

### How to Create Required Users

The required users (admin and basic) are created by running the `add_required_users.py` script.

## Setup Process

### Step 1: Import Database
```bash
# Import the database schema (without users)
mysql -u root sepik_database < database/database.sql
```

### Step 2: Create Required Users
```bash
# Run the user creation script
python add_required_users.py
```

This script will:
- Check if admin user exists
- Create admin user with properly hashed password if not exists
- Check if basic user exists  
- Create basic user with properly hashed password if not exists
- Create customer profile for basic user
- Display confirmation messages

### Step 3: Verify Users Created
```bash
# Check users in database
mysql -u root sepik_database -e "SELECT user_id, email, role FROM users;"
```

You should see:
```
+---------+-------+----------+
| user_id | email | role     |
+---------+-------+----------+
|       1 | admin | admin    |
|       2 | basic | customer |
+---------+-------+----------+
```

## Login Credentials

After running `add_required_users.py`:

**Admin Account:**
- Username: `admin`
- Password: `Pass@2026!`
- Role: Admin
- Access: Full system administration

**Basic Account:**
- Username: `basic`
- Password: `Pass@2026!`
- Role: Customer
- Access: Customer dashboard and features

## Using the PowerShell Script (Recommended)

The easiest way is to use the automated deployment script:

```powershell
.\run.ps1
```

This script automatically:
1. Checks Python installation
2. Creates virtual environment
3. Installs dependencies
4. Imports database (if needed)
5. **Runs add_required_users.py automatically**
6. Starts the application

## Manual Verification

### Test Admin Login
1. Start application: `python app.py`
2. Open browser: http://localhost:5000
3. Click "Login"
4. Enter: `admin` / `Pass@2026!`
5. Should redirect to admin dashboard

### Test Basic Login
1. Logout if logged in
2. Click "Login"
3. Enter: `basic` / `Pass@2026!`
4. Should redirect to customer dashboard

## Password Hashing Details

### How Bcrypt Works
```python
import bcrypt

# When creating a user
password = "Pass@2026!"
hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())

# When checking login
is_valid = bcrypt.checkpw(password.encode(), stored_hash)
```

### Why Each Hash is Different
Even for the same password, bcrypt generates different hashes:
```
Hash 1: $2b$12$abc123...
Hash 2: $2b$12$xyz789...
```

Both are valid for "Pass@2026!" but look different due to unique salts.

## Troubleshooting

### Problem: "User already exists" message
**Solution:** Users are already created. Try logging in.

### Problem: "Invalid email or password"
**Possible causes:**
1. Users not created yet - Run `python add_required_users.py`
2. Wrong password - Ensure you're using `Pass@2026!` (case-sensitive, with special characters)
3. Database not imported - Run database import first

### Problem: "Can't connect to database"
**Solution:**
1. Start MySQL/MariaDB service
2. Create database: `CREATE DATABASE sepik_database;`
3. Import schema: `mysql -u root sepik_database < database/database.sql`
4. Run user script: `python add_required_users.py`

### Problem: bcrypt module not found
**Solution:**
```bash
pip install bcrypt
# or
pip install -r requirements.txt
```

## For Assessors/Lecturers

### Quick Test
```powershell
# One command to set everything up
.\run.ps1

# When prompted, press Y to start application
# Then test login with admin/Pass@2026!
```

### Verify Password Hashing
```python
# Run this to see how passwords are hashed
python generate_password_hash.py
```

### Check Database
```bash
# View users table
mysql -u root sepik_database -e "SELECT user_id, first_name, last_name, email, role, is_active FROM users;"
```

## Security Notes

### Why This Approach is Secure
1. ✅ Passwords never stored in plain text
2. ✅ Bcrypt uses strong hashing algorithm
3. ✅ Unique salt for each password
4. ✅ Computationally expensive (prevents brute force)
5. ✅ Industry standard for password storage

### Password Requirements
- Minimum 6 characters (configurable in code)
- Current default: `Pass@2026!`
- Can be changed after first login via profile page
- Reset functionality available for admins

## Additional Users

### Creating More Users

**Via User Management Page (Admin):**
1. Login as admin
2. Navigate to "User Management"
3. Click "Add User"
4. Fill in details
5. Default password: `Pass@2026!`

**Via Registration Page (Customers):**
1. Go to http://localhost:5000/register
2. Fill in registration form
3. Choose your own password
4. Account created as customer role

**Via Python Script:**
```python
from models import User, Customer

# Create admin user
user_id = User.create(
    first='John',
    last='Doe',
    email='john@example.com',
    password='YourPassword123!',
    role='admin',
    phone='+675 1234567',
    address='Address here'
)

# Create customer user
user_id = User.create(
    first='Jane',
    last='Smith',
    email='jane@example.com',
    password='YourPassword123!',
    role='customer',
    phone='+675 7654321',
    address='Address here'
)
Customer.create(user_id)  # Create customer profile
```

## Summary

✅ **DO:** Run `python add_required_users.py` after importing database  
✅ **DO:** Use `.\run.ps1` for automated setup  
✅ **DO:** Test login with admin/Pass@2026! and basic/Pass@2026!  

❌ **DON'T:** Expect users to be in database.sql  
❌ **DON'T:** Try to manually insert password hashes  
❌ **DON'T:** Store plain text passwords anywhere  

---

**Questions?** Check the other documentation files:
- `PROJECT_SUBMISSION_README.md` - Complete guide
- `QUICK_START.md` - Quick reference
- `INSTALLATION_GUIDE.md` - Setup instructions
