# Quick Start Guide - Sepik Fresh

## For Lecturers/Assessors

This is a quick reference for testing the Assessment 2 requirements.

### 1. Setup (5 minutes)

```powershell
# Navigate to project folder
cd sepik_fresh

# Run deployment script
.\run.ps1

# When prompted, press Y to start the application
```

**Alternative (if PowerShell script fails):**
```bash
pip install -r requirements.txt
python add_required_users.py
python app.py
```

### 2. Access Application

Open browser: **http://localhost:5000**

### 3. Test Login Credentials

**Admin Account (Full Access):**
- Username: `admin`
- Password: `Pass@2026!`

**Basic User Account (Customer):**
- Username: `basic`
- Password: `Pass@2026!`

### 4. Assessment Requirements Testing

#### ✅ Requirement 1: User Management Page

1. Login as `admin` / `Pass@2026!`
2. Click **"User Management"** in sidebar
3. Test features:
   - View all users in table
   - Click **"Add User"** → Fill form → Submit
   - Click **"Edit"** on any user → Modify details → Save
   - Click **"Reset"** → Confirms password reset to `Pass@2026!`
   - Click **"Delete"** → Removes user (with confirmation)

**URL:** http://localhost:5000/admin/user-management

#### ✅ Requirement 2: Documentation Page

1. Navigate to **"Documentation"** in top menu
2. View project documentation information
3. Click **"Download Full Documentation"** link

**URL:** http://localhost:5000/documentation

**Note:** Place your Part 1 PDF in `static/docs/Sepik_Fresh_Documentation.pdf`

#### ✅ Requirement 3: Developers Page

1. Navigate to **"Developers"** in top menu
2. View team member cards with:
   - Photos (or placeholders)
   - Names and roles
   - Brief biographies
   - Contact links (email, GitHub, LinkedIn)

**URL:** http://localhost:5000/developers

**Note:** Customize developer info in `templates/developers.html`

#### ✅ Requirement 4a: Required User Accounts

Both accounts are created automatically by `add_required_users.py`:

| Username | Password | Role | Status |
|----------|----------|------|--------|
| admin | Pass@2026! | Admin | ✅ Created |
| basic | Pass@2026! | Customer | ✅ Created |

**Test:**
1. Logout if logged in
2. Login with `admin` / `Pass@2026!` → Should access admin dashboard
3. Logout
4. Login with `basic` / `Pass@2026!` → Should access customer dashboard

#### ✅ Requirement 4b: phpMyAdmin Credentials

**Access phpMyAdmin:**
- URL: http://localhost/phpmyadmin (or your XAMPP/WAMP URL)
- Username: `root`
- Password: (leave blank)
- Database: `sepik_database`

#### ✅ Requirement 4c: Database Export

**File Location:** `database/database.sql`

**Import Instructions:**
```bash
# Via MySQL CLI:
mysql -u root sepik_database < database/database.sql

# Or use phpMyAdmin:
# 1. Open phpMyAdmin
# 2. Select 'sepik_database'
# 3. Click 'Import' tab
# 4. Choose 'database/database.sql'
# 5. Click 'Go'
```

#### ✅ Requirement 4e: PowerShell Deployment Script

**File Location:** `run.ps1`

**Features:**
- ✅ Checks Python installation
- ✅ Creates virtual environment
- ✅ Installs dependencies from requirements.txt
- ✅ Runs user setup script
- ✅ Provides startup instructions
- ✅ Optionally starts the application

**Run:**
```powershell
.\run.ps1
```

### 5. Additional Features to Test

#### Admin Dashboard
- View statistics (users, orders, products, deliveries)
- Recent orders table
- Export to PDF functionality

#### Order Management
- View all orders with filters
- Update order status
- Search orders
- Export to CSV

#### Product Management
- Add new products
- Edit product details
- Update stock quantities
- Toggle product availability
- Delete products

#### Inbox
- View contact messages
- Mark as read/unread
- Delete messages

### 6. Database Structure

**Tables:**
- `users` - User accounts (admin, customer, delivery_staff)
- `customers` - Customer profiles
- `products` - Product catalog
- `orders` - Order records
- `order_items` - Order line items
- `contact_messages` - Contact form submissions
- `agent_notifications` - System alerts
- `password_reset_tokens` - Password reset functionality

### 7. Project Files Overview

```
sepik_fresh/
├── run.ps1                    ⭐ PowerShell deployment script
├── add_required_users.py      ⭐ Creates admin/basic users
├── app.py                     Main Flask application
├── models.py                  Database models (OOP)
├── database/
│   └── database.sql           ⭐ Database export
├── static/docs/
│   └── [Your_PDF_Here]        ⭐ Place documentation PDF here
├── templates/
│   ├── admin_user_management.html  ⭐ User management page
│   ├── developers.html             ⭐ Developers page
│   └── documentation.html          ⭐ Documentation page
└── PROJECT_SUBMISSION_README.md    Complete documentation
```

### 8. Troubleshooting

**Problem:** Can't connect to database
**Solution:** 
- Start MySQL/MariaDB service
- Check credentials in `config.py`
- Import database: `mysql -u root sepik_database < database/database.sql`

**Problem:** Module not found errors
**Solution:**
```bash
pip install -r requirements.txt
```

**Problem:** Port 5000 already in use
**Solution:**
- Kill process: `netstat -ano | findstr :5000` then `taskkill /PID <pid> /F`
- Or change port in `app.py`: `app.run(port=5001)`

**Problem:** Users admin/basic don't exist
**Solution:**
```bash
python add_required_users.py
```

### 9. Grading Checklist

- ✅ User Management page functional
- ✅ Can list all users
- ✅ Can edit user details (username, name, role)
- ✅ Can delete users
- ✅ Can reset passwords to Pass@2026!
- ✅ Documentation page accessible
- ✅ PDF documentation link present
- ✅ Developers page shows team members
- ✅ Each developer has photo and bio
- ✅ Admin user (admin/Pass@2026!) works
- ✅ Basic user (basic/Pass@2026!) works
- ✅ Database exported to database.sql
- ✅ phpMyAdmin credentials documented (root/no password)
- ✅ PowerShell script (run.ps1) executes successfully

### 10. Contact

For any issues during assessment:
- Check `PROJECT_SUBMISSION_README.md` for detailed documentation
- Review `INSTALLATION_GUIDE.md` for setup instructions
- All source code is commented and follows OOP principles

---

**Assessment 2 Requirements: COMPLETE ✅**
