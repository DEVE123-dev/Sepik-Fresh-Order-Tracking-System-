# Sepik Fresh Tracking System - Assessment 2 Submission

## Project Overview
Sepik Fresh is a comprehensive order tracking and delivery management system for fresh poultry and eggs from East Sepik Province, Papua New Guinea.

## Assessment Requirements Checklist

### ✅ 1. Admin Dashboard - User Management
**Location:** `/admin/user-management`

Features implemented:
- ✅ List all users with details (username, name, role, status)
- ✅ Edit user details (username, name, role)
- ✅ Delete user records
- ✅ Reset password to default (Pass@2026!)
- ✅ Add new users
- ✅ Toggle user active/inactive status

**Access:** Login as admin → Navigate to "User Management" in sidebar

### ✅ 2. Documentation Page
**Location:** `/documentation`

Features:
- ✅ Link to PDF documentation (Part 1 assessment)
- ✅ Accessible from home page navigation
- ✅ PDF file location: `sepik_fresh/static/docs/Sepik_Fresh_Documentation.pdf`

**Note:** Place your Part 1 PDF documentation in `static/docs/` folder

### ✅ 3. Developers Page
**Location:** `/developers`

Features:
- ✅ Displays all group members
- ✅ Photos for each member (with placeholder fallback)
- ✅ Brief write-up for each developer
- ✅ Contact information (email, GitHub, LinkedIn)
- ✅ Accessible from home page navigation

**Note:** Add developer photos to `static/images/` (dev1.jpg, dev2.jpg, etc.)

### ✅ 4. Required User Accounts

Two users with specified credentials:

| Username | Password | Role |
|----------|----------|------|
| admin | Pass@2026! | Admin |
| basic | Pass@2026! | Customer |

**Setup:** Run `python add_required_users.py` to create these users

### ✅ 5. Database Export
**Location:** `sepik_fresh/database/database.sql`

- ✅ Complete database schema
- ✅ Sample data included
- ✅ Ready for import via phpMyAdmin or MySQL CLI

**phpMyAdmin Credentials:**
- Username: `root`
- Password: (none)
- Database: `sepik_database`

### ✅ 6. Deployment Script
**Location:** `sepik_fresh/run.ps1`

PowerShell script that:
- ✅ Checks Python installation
- ✅ Creates virtual environment
- ✅ Installs dependencies
- ✅ Sets up required users
- ✅ Provides startup instructions

**Usage:** 
```powershell
cd sepik_fresh
.\run.ps1
```

## Project Structure

```
sepik_fresh/
├── app.py                          # Main Flask application
├── models.py                       # Database models (OOP)
├── config.py                       # Configuration settings
├── agents.py                       # Background monitoring agents
├── email_utils.py                  # Email notification system
├── requirements.txt                # Python dependencies
├── run.ps1                         # PowerShell deployment script
├── add_required_users.py           # Script to add admin/basic users
├── database/
│   ├── database.sql                # Complete database export
│   ├── sepik_database.sql          # Original schema
│   └── sepik_fresh.db              # SQLite backup (if needed)
├── static/
│   ├── css/                        # Stylesheets
│   ├── js/                         # JavaScript files
│   ├── images/                     # Images and logos
│   └── docs/                       # Documentation PDFs
│       └── Sepik_Fresh_Documentation.pdf  # ⚠️ ADD YOUR PDF HERE
├── templates/                      # HTML templates
│   ├── home.html
│   ├── developers.html             # NEW: Developers page
│   ├── documentation.html          # NEW: Documentation page
│   ├── admin_user_management.html  # NEW: User management
│   ├── dashboard_admin.html
│   ├── dashboard_customer.html
│   ├── dashboard_staff.html
│   └── ... (other templates)
└── tests/                          # Unit tests
```

## Installation & Deployment

### Method 1: Using PowerShell Script (Recommended)
```powershell
cd sepik_fresh
.\run.ps1
```

### Method 2: Manual Setup
```bash
# 1. Create virtual environment
python -m venv venv

# 2. Activate virtual environment
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Import database
mysql -u root sepik_database < database/database.sql

# 5. Add required users
python add_required_users.py

# 6. Run application
python app.py
```

## Access the Application

**URL:** http://localhost:5000

### Login Credentials

**Admin Account:**
- Username: `admin`
- Password: `Pass@2026!`
- Access: Full system administration

**Basic User Account:**
- Username: `basic`
- Password: `Pass@2026!`
- Access: Customer features

**Test Accounts (from database):**
- Email: `penningtonakamiau@gmail.com` / Password: (existing)
- Email: `ishojonduo@gmail.com` / Password: (existing)
- Email: `benjaminbino19@gmail.com` / Password: (existing)

## Key Features

### For Customers
- ✅ User registration and authentication
- ✅ Browse available products
- ✅ Place orders with multiple items
- ✅ Real-time order tracking
- ✅ Order history and status updates
- ✅ Profile management
- ✅ Password reset functionality
- ✅ Email notifications

### For Admin
- ✅ Dashboard with statistics
- ✅ Order management (view, update status, export)
- ✅ Product management (add, edit, delete, stock control)
- ✅ **User management (add, edit, delete, reset passwords)** ⭐ NEW
- ✅ Inbox for contact messages
- ✅ System alerts and notifications
- ✅ CSV export functionality
- ✅ PDF export for reports

### For Delivery Staff
- ✅ View assigned deliveries
- ✅ Update delivery status
- ✅ Track active orders

## Technology Stack

- **Backend:** Python 3.8+, Flask
- **Database:** MySQL/MariaDB
- **Frontend:** HTML5, CSS3, JavaScript
- **Authentication:** bcrypt password hashing
- **Email:** SMTP (Gmail)
- **PDF Generation:** jsPDF
- **Icons:** Font Awesome 6.5.0

## Database Configuration

**File:** `config.py`

```python
DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'password': '',  # No password for root
    'database': 'sepik_database'
}
```

## Testing

Run unit tests:
```bash
python run_tests.py
```

## Important Notes for Submission

1. **📄 Add Your Documentation PDF**
   - Place your Part 1 documentation in: `static/docs/Sepik_Fresh_Documentation.pdf`

2. **👥 Add Developer Photos (Optional)**
   - Add team member photos: `static/images/dev1.jpg`, `dev2.jpg`, etc.
   - Update names and bios in `templates/developers.html`

3. **🗄️ Database Setup**
   - Ensure MySQL/MariaDB is running
   - Import `database/database.sql` via phpMyAdmin or CLI
   - Run `add_required_users.py` to create admin/basic accounts

4. **🔐 Login Credentials**
   - Admin: `admin` / `Pass@2026!`
   - Basic: `basic` / `Pass@2026!`

## Troubleshooting

### Database Connection Error
```
Error: Can't connect to MySQL server
```
**Solution:** Ensure MySQL/MariaDB is running and credentials in `config.py` are correct

### Module Not Found Error
```
ModuleNotFoundError: No module named 'flask'
```
**Solution:** Activate virtual environment and run `pip install -r requirements.txt`

### Port Already in Use
```
OSError: [Errno 98] Address already in use
```
**Solution:** Change port in `app.py` or kill process using port 5000

## Contact & Support

For questions or issues:
- Check the documentation page: http://localhost:5000/documentation
- View developer information: http://localhost:5000/developers
- Contact admin: admin@sepikfresh.com

## License

© 2026 Sepik Fresh. All rights reserved.

---

**Submission Checklist:**
- ✅ User Management page implemented
- ✅ Documentation page created
- ✅ Developers page created
- ✅ Admin and basic users configured
- ✅ Database exported to database.sql
- ✅ PowerShell deployment script (run.ps1)
- ⚠️ Add your PDF documentation to static/docs/
- ⚠️ Update developer information in developers.html
- ⚠️ Test all features before submission
