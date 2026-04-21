# 📋 Submission Checklist - Assessment 2

## Before You Submit - Complete This Checklist

### 📁 Required Files

- [x] `run.ps1` - PowerShell deployment script
- [x] `database/database.sql` - Database export
- [x] `add_required_users.py` - User creation script
- [ ] `static/docs/Sepik_Fresh_Documentation.pdf` - **⚠️ ADD YOUR PDF HERE**
- [x] `templates/admin_user_management.html` - User management page
- [x] `templates/developers.html` - Developers page
- [x] `templates/documentation.html` - Documentation page

### 👥 Required User Accounts

Run this command to create required users:
```bash
python add_required_users.py
```

Then verify:
- [ ] Login with `admin` / `Pass@2026!` works
- [ ] Login with `basic` / `Pass@2026!` works
- [ ] Admin user has full access to admin dashboard
- [ ] Basic user has customer dashboard access

### 🎯 Feature Testing

#### 1. User Management (Admin Dashboard)
- [ ] Navigate to `/admin/user-management`
- [ ] Can view all users in table
- [ ] Click "Add User" button - modal opens
- [ ] Fill form and add new user - success message appears
- [ ] Click "Edit" on a user - modal opens with user data
- [ ] Modify user details and save - success message appears
- [ ] Click "Reset" on a user - password resets to Pass@2026!
- [ ] Click "Delete" on a user - confirmation dialog appears
- [ ] Confirm deletion - user removed from list

#### 2. Documentation Page
- [ ] Navigate to `/documentation` from main menu
- [ ] Page loads with professional layout
- [ ] "Download Full Documentation" link is visible
- [ ] PDF file exists at `static/docs/Sepik_Fresh_Documentation.pdf`
- [ ] Click download link - PDF downloads successfully

#### 3. Developers Page
- [ ] Navigate to `/developers` from main menu
- [ ] Page displays team member cards
- [ ] Each card shows: photo, name, role, bio
- [ ] Contact icons (email, GitHub, LinkedIn) are visible
- [ ] Hover effects work on cards
- [ ] Responsive layout works on mobile

#### 4. Database
- [ ] MySQL/MariaDB is running
- [ ] Database `sepik_database` exists
- [ ] Import `database/database.sql` successfully
- [ ] All tables created (users, customers, products, orders, etc.)
- [ ] Sample data loaded correctly

#### 5. Deployment Script
- [ ] Run `.\run.ps1` in PowerShell
- [ ] Script checks Python installation
- [ ] Script creates virtual environment
- [ ] Script installs dependencies
- [ ] Script creates required users
- [ ] No errors during execution
- [ ] Application starts successfully

### 📝 Customization Tasks

#### Update Developer Information
Edit `templates/developers.html`:
- [ ] Replace "John Doe" with actual team member 1 name
- [ ] Replace "Jane Smith" with actual team member 2 name
- [ ] Replace "Michael Johnson" with actual team member 3 name
- [ ] Replace "Sarah Williams" with actual team member 4 name
- [ ] Update roles for each member
- [ ] Update biographies for each member
- [ ] Update email addresses
- [ ] Update GitHub links
- [ ] Update LinkedIn links

#### Add Developer Photos (Optional)
Add to `static/images/`:
- [ ] `dev1.jpg` - Team member 1 photo (150x150px recommended)
- [ ] `dev2.jpg` - Team member 2 photo
- [ ] `dev3.jpg` - Team member 3 photo
- [ ] `dev4.jpg` - Team member 4 photo

*Note: If photos not provided, placeholder images will display automatically*

#### Add Documentation PDF
- [ ] Place your Part 1 PDF in `static/docs/`
- [ ] Rename it to `Sepik_Fresh_Documentation.pdf`
- [ ] Verify file size is reasonable (< 10MB recommended)
- [ ] Test download link works

### 🔧 Technical Verification

#### Database Configuration
Check `config.py`:
- [ ] Host: `localhost`
- [ ] User: `root`
- [ ] Password: `` (empty)
- [ ] Database: `sepik_database`

#### Dependencies
- [ ] `requirements.txt` exists
- [ ] All packages install without errors
- [ ] Virtual environment activates correctly

#### Application Startup
- [ ] Run `python app.py`
- [ ] No import errors
- [ ] No database connection errors
- [ ] Server starts on port 5000
- [ ] Can access http://localhost:5000

### 📊 Assessment Requirements Verification

| # | Requirement | Status | Evidence |
|---|-------------|--------|----------|
| 1 | User Management - List users | [ ] | Navigate to /admin/user-management |
| 2 | User Management - Edit users | [ ] | Click Edit button, modify, save |
| 3 | User Management - Delete users | [ ] | Click Delete button, confirm |
| 4 | User Management - Reset password | [ ] | Click Reset button |
| 5 | Documentation page exists | [ ] | Navigate to /documentation |
| 6 | Documentation PDF link | [ ] | Click download link |
| 7 | Developers page exists | [ ] | Navigate to /developers |
| 8 | Developer photos displayed | [ ] | View team member cards |
| 9 | Developer bios included | [ ] | Read descriptions |
| 10 | Admin user (admin/Pass@2026!) | [ ] | Login successfully |
| 11 | Basic user (basic/Pass@2026!) | [ ] | Login successfully |
| 12 | phpMyAdmin credentials documented | [ ] | root/(no password) |
| 13 | Database exported to database.sql | [ ] | File exists in database/ folder |
| 14 | PowerShell script (run.ps1) | [ ] | Execute successfully |

### 🚀 Final Steps

1. **Test Complete Workflow**
   ```powershell
   # Start fresh
   cd sepik_fresh
   
   # Run deployment script
   .\run.ps1
   
   # When prompted, start application
   # Press Y
   ```

2. **Test All Features**
   - [ ] Open http://localhost:5000
   - [ ] Test navigation menu
   - [ ] Login as admin
   - [ ] Test user management
   - [ ] Check documentation page
   - [ ] Check developers page
   - [ ] Logout and login as basic user
   - [ ] Verify customer features work

3. **Review Documentation**
   - [ ] Read `PROJECT_SUBMISSION_README.md`
   - [ ] Read `QUICK_START.md`
   - [ ] Verify all instructions are clear

4. **Clean Up**
   - [ ] Remove any test data you don't want to submit
   - [ ] Ensure no sensitive information in code
   - [ ] Check all files are properly formatted
   - [ ] Remove any unnecessary files

### 📦 Submission Package

Your submission should include:

```
sepik_fresh/
├── run.ps1                              ✅ PowerShell script
├── add_required_users.py                ✅ User setup script
├── app.py                               ✅ Main application
├── models.py                            ✅ Database models
├── config.py                            ✅ Configuration
├── requirements.txt                     ✅ Dependencies
├── database/
│   └── database.sql                     ✅ Database export
├── static/
│   ├── css/                             ✅ Stylesheets
│   ├── js/                              ✅ JavaScript
│   ├── images/                          ✅ Images + dev photos
│   └── docs/
│       └── Sepik_Fresh_Documentation.pdf ⚠️ ADD THIS
├── templates/
│   ├── admin_user_management.html       ✅ User management
│   ├── developers.html                  ✅ Developers page
│   ├── documentation.html               ✅ Documentation page
│   └── ... (all other templates)        ✅ Existing templates
├── PROJECT_SUBMISSION_README.md         ✅ Complete guide
├── QUICK_START.md                       ✅ Quick reference
└── SUBMISSION_CHECKLIST.md              ✅ This file
```

### ⚠️ Common Issues & Solutions

**Issue:** Can't connect to database
```bash
# Solution: Start MySQL/MariaDB
# Windows (XAMPP): Start from XAMPP Control Panel
# Import database: mysql -u root sepik_database < database/database.sql
```

**Issue:** Module not found errors
```bash
# Solution: Install dependencies
pip install -r requirements.txt
```

**Issue:** Users admin/basic don't exist
```bash
# Solution: Run user creation script
python add_required_users.py
```

**Issue:** Port 5000 already in use
```bash
# Solution: Change port in app.py
# Or kill existing process
```

### ✅ Final Verification

Before submitting, answer these questions:

- [ ] Can I run `.\run.ps1` without errors?
- [ ] Can I login with admin/Pass@2026!?
- [ ] Can I login with basic/Pass@2026!?
- [ ] Does user management page work completely?
- [ ] Does documentation page display correctly?
- [ ] Does developers page show team information?
- [ ] Is my PDF documentation in the correct location?
- [ ] Have I customized developer information?
- [ ] Does database.sql import successfully?
- [ ] Have I tested all features?

### 📧 Submission

When all items are checked:

1. **Create submission package**
   - Zip the entire `sepik_fresh` folder
   - Name it: `YourName_IT0303_Assessment2.zip`

2. **Include in submission**
   - Zipped project folder
   - Any additional documentation required
   - Screenshots (if requested)

3. **Double-check**
   - All files included
   - No sensitive information
   - README files are clear
   - Code is well-commented

---

## 🎉 Ready to Submit!

Once all checkboxes are marked, your project is ready for submission.

**Good luck with your assessment!** 🚀

---

**Need Help?**
- Review `PROJECT_SUBMISSION_README.md` for detailed information
- Check `QUICK_START.md` for quick reference
- Review `INSTALLATION_GUIDE.md` for setup help
