# Sepik Fresh - Setup Instructions for New Users

## 📦 What You Received

You have received the complete Sepik Fresh Order Tracking System project. This guide will help you set it up on your computer.

---

## 🎯 Quick Start (5 Minutes)

### Prerequisites

Before starting, make sure you have:
- ✅ Python 3.7 or higher installed
- ✅ MySQL or MariaDB installed (with phpMyAdmin)
- ✅ A code editor (VS Code, PyCharm, etc.)

---

## 🚀 Setup Steps

### Step 1: Extract the Project

1. Extract the ZIP file to a folder on your computer
2. You should see a folder structure like this:
   ```
   sepik-fresh/
   ├── sepik_fresh/
   ├── docs/
   ├── README.md
   └── SETUP_INSTRUCTIONS.md (this file)
   ```

### Step 2: Open in Your IDE

**For VS Code:**
1. Open VS Code
2. File → Open Folder
3. Select the `sepik-fresh` folder
4. Click "Select Folder"

**For PyCharm:**
1. Open PyCharm
2. File → Open
3. Select the `sepik-fresh` folder
4. Click "OK"

### Step 3: Install Python Dependencies

Open terminal in your IDE and run:

```bash
cd sepik_fresh
pip install -r requirements.txt
```

**Wait for installation to complete** (may take 1-2 minutes)

### Step 4: Setup Database

#### Option A: Using phpMyAdmin (Recommended)

1. Open phpMyAdmin in your browser: `http://localhost/phpmyadmin`
2. Click "New" to create a database
3. Database name: `sepik_database`
4. Click "Create"
5. Click "Import" tab
6. Click "Choose File"
7. Navigate to: `sepik_fresh/database/database.sql`
8. Click "Go" at the bottom
9. Wait for success message ✓

#### Option B: Using MySQL Command Line

```bash
mysql -u root -p
CREATE DATABASE sepik_database;
USE sepik_database;
SOURCE sepik_fresh/database/database.sql;
EXIT;
```

### Step 5: Configure Database Connection

1. Open `sepik_fresh/config.py`
2. Update database credentials if needed:
   ```python
   DB_HOST = 'localhost'
   DB_USER = 'root'          # Your MySQL username
   DB_PASSWORD = ''          # Your MySQL password
   DB_NAME = 'sepik_database'
   ```

### Step 6: Create Required Users

In your terminal, run:

```bash
cd sepik_fresh
python add_required_users.py
```

You should see:
```
✓ Admin user created successfully!
✓ Basic user created successfully!
```

### Step 7: Update Product Images (Optional)

If you want to see product images:

1. Run this SQL in phpMyAdmin:
   ```sql
   USE sepik_database;
   SOURCE sepik_fresh/database/update_image_paths.sql;
   ```

   Or manually run:
   ```sql
   UPDATE products SET image_url = '/static/images/products/wholefreshchicken.jpg' WHERE product_id = 2;
   UPDATE products SET image_url = '/static/images/products/chickenpieces.jpg' WHERE product_id = 3;
   UPDATE products SET image_url = '/static/images/products/30eggs.jpg' WHERE product_id = 4;
   UPDATE products SET image_url = '/static/images/products/dozeneggs.jpg' WHERE product_id = 5;
   ```

### Step 8: Start the Application

In your terminal:

```bash
cd sepik_fresh
python app.py
```

You should see:
```
* Running on http://127.0.0.1:5000
* Running on http://localhost:5000
```

### Step 9: Access the Application

1. Open your web browser
2. Go to: `http://localhost:5000`
3. You should see the Sepik Fresh home page! 🎉

---

## 🔐 Login Credentials

### Admin Account
- **Username:** `admin`
- **Password:** `Pass@2026!`
- **Access:** Full system access

### Customer Account
- **Username:** `basic`
- **Password:** `Pass@2026!`
- **Access:** Customer features

### Additional Accounts (Already in Database)
- **Email:** `ishojonduo@gmail.com` / **Password:** `Pass@2026!` (Admin)
- **Email:** `penningtonakamiau@gmail.com` / **Password:** `Pass@2026!` (Delivery Staff)
- **Email:** `benjaminbino19@gmail.com` / **Password:** `Pass@2026!` (Delivery Staff)

---

## 🧪 Testing the System

### Test Admin Features
1. Login with `admin` / `Pass@2026!`
2. You should see the Admin Dashboard
3. Try:
   - View Products
   - View Orders
   - Manage Users
   - View Contact Messages

### Test Customer Features
1. Logout
2. Login with `basic` / `Pass@2026!`
3. You should see the Customer Dashboard
4. Try:
   - Browse Products
   - Place an Order
   - Track Orders
   - Edit Profile

---

## 📁 Project Structure

```
sepik-fresh/
│
├── sepik_fresh/              # Main application folder
│   ├── app.py               # Main Flask application
│   ├── models.py            # Database models (OOP)
│   ├── config.py            # Configuration
│   ├── requirements.txt     # Python dependencies
│   │
│   ├── database/            # Database files
│   │   ├── database.sql    # Main database file
│   │   └── README.txt      # Database setup guide
│   │
│   ├── static/              # Static files (CSS, JS, images)
│   │   ├── css/
│   │   ├── js/
│   │   └── images/
│   │
│   └── templates/           # HTML templates
│
├── docs/                    # Documentation
│   ├── QUICK_START.md
│   ├── INSTALLATION_GUIDE.md
│   └── ... (more docs)
│
├── README.md                # Main project documentation
└── SETUP_INSTRUCTIONS.md    # This file
```

---

## 🔧 Troubleshooting

### Problem: "Module not found" error

**Solution:**
```bash
cd sepik_fresh
pip install -r requirements.txt
```

### Problem: "Can't connect to MySQL server"

**Solution:**
1. Make sure MySQL/MariaDB is running
2. Check credentials in `config.py`
3. Test connection:
   ```bash
   mysql -u root -p
   ```

### Problem: "Database 'sepik_database' doesn't exist"

**Solution:**
1. Open phpMyAdmin
2. Create database: `sepik_database`
3. Import: `sepik_fresh/database/database.sql`

### Problem: "Invalid email or password" when logging in

**Solution:**
```bash
cd sepik_fresh
python add_required_users.py
```

### Problem: Port 5000 already in use

**Solution:**
```bash
# Use a different port
python app.py --port 5001
```

Or kill the process using port 5000:
```bash
# Windows
netstat -ano | findstr :5000
taskkill /PID <PID> /F

# Linux/Mac
lsof -ti:5000 | xargs kill -9
```

### Problem: Images not showing

**Solution:**
1. Check files exist in `sepik_fresh/static/images/products/`
2. Run: `sepik_fresh/database/update_image_paths.sql`
3. Refresh browser (Ctrl+F5)

---

## 📚 Additional Resources

### Documentation
- **Main README:** `README.md` - Complete project overview
- **Quick Start:** `docs/QUICK_START.md` - Fast setup guide
- **Installation Guide:** `docs/INSTALLATION_GUIDE.md` - Detailed setup
- **Product Images:** `sepik_fresh/START_HERE.txt` - Image setup guide

### Quick Reference Files
- `sepik_fresh/START_HERE.txt` - Quick image setup
- `sepik_fresh/IMAGE_PATHS_REFERENCE.txt` - Image path reference
- `sepik_fresh/IMPORTANT_PASSWORD_INFO.txt` - Password information

---

## 🎓 For Assessors/Teachers

### Quick Assessment Setup

1. **Extract project**
2. **Open terminal in `sepik_fresh` folder**
3. **Run automated setup:**
   ```bash
   # Windows PowerShell
   .\run.ps1
   
   # Linux/Mac
   ./install.sh
   ```
4. **Wait for setup to complete**
5. **Press Y to start application**
6. **Open browser:** `http://localhost:5000`
7. **Login:** `admin` / `Pass@2026!`

**Total time:** ~3-5 minutes

### What to Test

- ✅ Admin login and dashboard
- ✅ Customer login and dashboard
- ✅ Product browsing with images
- ✅ Order placement
- ✅ Order tracking
- ✅ User management
- ✅ Responsive design (mobile view)

---

## 💡 Tips for Success

1. **Read README.md first** - It has everything you need
2. **Use the automated setup** - Run `run.ps1` (Windows) or `install.sh` (Linux/Mac)
3. **Check documentation** - All guides are in the `docs/` folder
4. **Test both accounts** - Try admin and customer features
5. **Check the slideshow** - Home page has product slideshow

---

## 🆘 Need Help?

1. Check `README.md` for detailed information
2. Check `docs/` folder for specific guides
3. Check troubleshooting section above
4. Review error messages carefully
5. Verify all prerequisites are installed

---

## ✅ Setup Checklist

Use this checklist to verify your setup:

- [ ] Python 3.7+ installed
- [ ] MySQL/MariaDB installed
- [ ] Project extracted
- [ ] Opened in IDE
- [ ] Dependencies installed (`pip install -r requirements.txt`)
- [ ] Database created (`sepik_database`)
- [ ] Database imported (`database.sql`)
- [ ] Config updated (`config.py`)
- [ ] Users created (`python add_required_users.py`)
- [ ] Application started (`python app.py`)
- [ ] Browser opened (`http://localhost:5000`)
- [ ] Admin login works (`admin` / `Pass@2026!`)
- [ ] Customer login works (`basic` / `Pass@2026!`)

---

## 🎉 Success!

If you can:
- ✅ See the home page
- ✅ Login as admin
- ✅ Login as customer
- ✅ Browse products
- ✅ Place an order

**Congratulations! Setup is complete!** 🎊

---

## 📞 Project Information

- **Project:** Sepik Fresh Order Tracking System
- **Version:** 1.0
- **Date:** April 2026
- **Technology:** Python Flask, MySQL, HTML/CSS/JavaScript

---

**Made with ❤️ for Sepik Fresh**

*For more information, see README.md in the project root.*
