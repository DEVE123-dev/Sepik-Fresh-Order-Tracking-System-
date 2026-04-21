# Sepik Fresh - Order Tracking System

> **Real-time visibility, reliable delivery.**

A comprehensive web-based order tracking and management system for Sepik Fresh, delivering fresh poultry and eggs from East Sepik Province, Papua New Guinea.

---

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Quick Start](#quick-start)
- [Product Images Setup](#product-images-setup)
- [User Roles](#user-roles)
- [Technology Stack](#technology-stack)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Documentation](#documentation)
- [Testing](#testing)
- [Deployment](#deployment)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)
- [License](#license)

---

## 🎯 Overview

Sepik Fresh is a full-featured order tracking system designed for fresh produce delivery businesses. It provides real-time order tracking, role-based access control, automated notifications, and a professional customer-facing interface.

### Key Highlights

- **Role-Based Access**: Admin, Delivery Staff, and Customer roles
- **Real-Time Tracking**: Track orders from placement to delivery
- **Product Management**: Full CRUD operations with image support
- **Automated Alerts**: AI-powered delivery monitoring
- **Responsive Design**: Works on desktop, tablet, and mobile
- **Email Notifications**: Order confirmations and status updates
- **Product Slideshow**: Engaging home page with featured products

---

## ✨ Features

### For Customers
- 🛒 Browse products with images
- 📦 Place orders online
- 🔍 Track order status in real-time
- 📧 Receive email notifications
- 👤 Manage profile and order history
- 📱 Mobile-responsive interface

### For Administrators
- 📊 Dashboard with key metrics
- 👥 User management (add, edit, delete)
- 📦 Order management and status updates
- 🏷️ Product management with images
- 📨 Contact message inbox
- 📈 Export data to CSV
- 🔔 Automated delivery alerts

### For Delivery Staff
- 🚚 View assigned deliveries
- ✅ Update delivery status
- 📋 Active delivery dashboard

---

## 🚀 Quick Start

### Prerequisites
- Python 3.7+
- MySQL/MariaDB
- pip (Python package manager)

### Installation (5 minutes)

1. **Clone or download the project**
   ```bash
   cd sepik_fresh
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Setup database**
   - Create database in phpMyAdmin: `sepik_database`
   - Import: `database/sepik_database.sql`
   - Run updates: `database/updates.sql`

4. **Configure settings**
   ```bash
   cp .env.example .env
   # Edit .env with your database credentials
   ```

5. **Run the application**
   ```bash
   python app.py
   ```

6. **Access the system**
   - Open browser: `http://localhost:5000`
   - Admin login: `ishojonduo@gmail.com` / `Pass@2026!`

---

## 🖼️ Product Images Setup

### Simple 3-Step Process

#### Step 1: Add Database Column
Run this SQL in phpMyAdmin:
```sql
ALTER TABLE products 
ADD COLUMN IF NOT EXISTS image_url VARCHAR(500) DEFAULT NULL 
AFTER description;
```

#### Step 2: Add Your Images
Put image files here:
```
sepik_fresh/static/images/products/
```
Example: `chicken.jpg`, `eggs.jpg`, `chicken_pieces.jpg`

#### Step 3: Link Images to Products
```sql
UPDATE products SET image_url = '/static/images/products/chicken.jpg' WHERE product_id = 2;
UPDATE products SET image_url = '/static/images/products/chicken_pieces.jpg' WHERE product_id = 3;
UPDATE products SET image_url = '/static/images/products/egg_tray.jpg' WHERE product_id = 4;
UPDATE products SET image_url = '/static/images/products/eggs_dozen.jpg' WHERE product_id = 5;
```

**Done!** Images will appear on:
- ✅ Products page
- ✅ Order form
- ✅ Home page slideshow

### Image Path Format
Always use: `/static/images/products/YOUR_IMAGE.jpg`

**See detailed guide:** `sepik_fresh/START_HERE.txt`

---

## 👥 User Roles

### Admin
- Full system access
- User management
- Product management
- Order management
- View reports and analytics
- Manage contact messages

**Default Admin:**
- Email: `ishojonduo@gmail.com`
- Password: `Pass@2026!`

### Delivery Staff
- View assigned deliveries
- Update delivery status
- Access delivery dashboard

**Default Staff:**
- Email: `penningtonakamiau@gmail.com`
- Password: `Pass@2026!`

### Customer
- Browse products
- Place orders
- Track orders
- Manage profile
- View order history

**Register:** `/register` page

---

## 🛠️ Technology Stack

### Backend
- **Python 3.7+** - Core language
- **Flask** - Web framework
- **MySQL/MariaDB** - Database
- **bcrypt** - Password hashing
- **mysql-connector-python** - Database connector

### Frontend
- **HTML5** - Structure
- **CSS3** - Styling
- **JavaScript** - Interactivity
- **Font Awesome** - Icons

### Features
- **OOP Design** - Model classes for all entities
- **Session Management** - Secure user sessions
- **Email Integration** - SMTP notifications
- **AI Agents** - Automated monitoring (optional)
- **CSV Export** - Data export functionality

---

## 📦 Installation

### Detailed Installation Steps

#### 1. System Requirements
- Python 3.7 or higher
- MySQL 5.7+ or MariaDB 10.3+
- 100MB disk space
- Modern web browser

#### 2. Database Setup

**Option A: Using phpMyAdmin**
1. Create database: `sepik_database`
2. Import `database/sepik_database.sql`
3. Import `database/updates.sql`
4. Import `database/add_product_images.sql` (for images)

**Option B: Using MySQL CLI**
```bash
mysql -u root -p
CREATE DATABASE sepik_database;
USE sepik_database;
SOURCE database/sepik_database.sql;
SOURCE database/updates.sql;
SOURCE database/add_product_images.sql;
```

#### 3. Python Dependencies
```bash
cd sepik_fresh
pip install -r requirements.txt
```

**Dependencies include:**
- Flask
- mysql-connector-python
- bcrypt
- python-dotenv
- gunicorn (for production)

#### 4. Configuration

**Create `.env` file:**
```bash
cp .env.example .env
```

**Edit `.env`:**
```env
# Database Configuration
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=your_password
DB_NAME=sepik_database

# Flask Configuration
SECRET_KEY=your-secret-key-here
FLASK_ENV=development

# Email Configuration (optional)
MAIL_SERVER=smtp.gmail.com
MAIL_PORT=587
MAIL_USERNAME=your-email@gmail.com
MAIL_PASSWORD=your-app-password
```

#### 5. Initialize Required Users
```bash
python add_required_users.py
```

This creates default admin and staff accounts.

#### 6. Run Application

**Development:**
```bash
python app.py
```

**Production:**
```bash
gunicorn -c gunicorn_config.py wsgi:app
```

---

## ⚙️ Configuration

### Database Configuration
Edit `config.py` or use environment variables:
```python
DB_HOST = 'localhost'
DB_USER = 'root'
DB_PASSWORD = 'your_password'
DB_NAME = 'sepik_database'
```

### Email Configuration
For email notifications, configure SMTP settings in `.env`:
```env
MAIL_SERVER=smtp.gmail.com
MAIL_PORT=587
MAIL_USE_TLS=True
MAIL_USERNAME=your-email@gmail.com
MAIL_PASSWORD=your-app-password
```

**Gmail Setup:**
1. Enable 2-factor authentication
2. Generate app password
3. Use app password in configuration

### Session Configuration
```python
SECRET_KEY = 'your-secret-key'
PERMANENT_SESSION_LIFETIME = timedelta(hours=2)
```

---

## 📖 Usage

### Customer Workflow

1. **Register Account**
   - Go to `/register`
   - Fill in details
   - Submit form

2. **Browse Products**
   - View products at `/products`
   - See images, prices, stock

3. **Place Order**
   - Go to `/order/new`
   - Select products and quantities
   - Confirm order

4. **Track Order**
   - View order status at `/my-orders`
   - Click order to see details
   - Receive email updates

### Admin Workflow

1. **Login**
   - Email: `ishojonduo@gmail.com`
   - Password: `Pass@2026!`

2. **Manage Products**
   - Add new products
   - Update prices and stock
   - Add product images
   - Enable/disable products

3. **Manage Orders**
   - View all orders
   - Update order status
   - Export to CSV

4. **Manage Users**
   - Add new users
   - Edit user details
   - Activate/deactivate accounts
   - Reset passwords

### Adding Product Images

**Method 1: Manual (Recommended)**
1. Save image to `static/images/products/`
2. Run SQL:
   ```sql
   UPDATE products 
   SET image_url = '/static/images/products/YOUR_IMAGE.jpg' 
   WHERE product_id = X;
   ```

**See:** `sepik_fresh/START_HERE.txt` for detailed guide

---

## 📚 Documentation

All documentation is organized in the `docs/` folder:

### Setup Guides
- **INSTALLATION_GUIDE.md** - Detailed installation instructions
- **QUICK_START.md** - Get started in 5 minutes
- **SETUP_PRODUCT_IMAGES.md** - Product images setup

### Feature Documentation
- **PRODUCT_IMAGES_FEATURE.md** - Product images feature details
- **ENHANCEMENTS_ADDED.md** - List of enhancements
- **IMPLEMENTATION_COMPLETE.md** - Implementation summary

### Reference
- **MANUAL_IMAGE_SETUP_GUIDE.md** - Manual image management
- **AGENT_TESTING_GUIDE.md** - AI agents testing
- **PASSWORD_SETUP_GUIDE.md** - Password management

### Planning Documents
- **AGILE_PLANNING.md** - Agile methodology
- **USER_STORIES.md** - User stories
- **STAKEHOLDER_ANALYSIS.md** - Stakeholder analysis
- **UML_DIAGRAMS.md** - System diagrams

### Quick Reference Files (in sepik_fresh/)
- **START_HERE.txt** - Simplest setup guide
- **IMAGE_PATHS_REFERENCE.txt** - Image path reference
- **FOLDER_STRUCTURE_GUIDE.txt** - Folder structure
- **QUICK_START_IMAGES.txt** - Quick image setup

---

## 🧪 Testing

### Manual Testing

**Test User Accounts:**
- Admin: `ishojonduo@gmail.com` / `Pass@2026!`
- Staff: `penningtonakamiau@gmail.com` / `Pass@2026!`
- Customer: Register new account

**Test Scenarios:**
1. Customer registration and login
2. Product browsing with images
3. Order placement
4. Order tracking
5. Admin product management
6. Admin order management
7. Email notifications
8. Responsive design (mobile/tablet)

### Automated Testing
```bash
python run_tests.py
```

**Test Coverage:**
- Model tests (`tests/test_models.py`)
- Route tests (`tests/test_routes.py`)

### Testing Checklist
See `docs/TESTING_CHECKLIST.md` for comprehensive testing checklist.

---

## 🚀 Deployment

### Production Deployment

#### 1. Prepare Environment
```bash
# Set production environment
export FLASK_ENV=production

# Update .env.production
cp .env.example .env.production
# Edit with production settings
```

#### 2. Database Setup
- Create production database
- Import schema
- Configure secure credentials
- Enable SSL connections

#### 3. Web Server Setup

**Using Gunicorn:**
```bash
gunicorn -c gunicorn_config.py wsgi:app
```

**Using Nginx (Reverse Proxy):**
```nginx
server {
    listen 80;
    server_name your-domain.com;

    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }

    location /static {
        alias /path/to/sepik_fresh/static;
    }
}
```

#### 4. Security Checklist
- [ ] Change default passwords
- [ ] Use strong SECRET_KEY
- [ ] Enable HTTPS
- [ ] Configure firewall
- [ ] Set up backups
- [ ] Enable error logging
- [ ] Restrict database access

#### 5. Performance Optimization
- Enable caching
- Optimize images
- Use CDN for static files
- Configure database connection pooling

---

## 🔧 Troubleshooting

### Common Issues

#### Database Connection Error
**Problem:** `Can't connect to MySQL server`

**Solution:**
1. Check MySQL is running
2. Verify credentials in `.env`
3. Check database exists
4. Test connection: `mysql -u root -p`

#### Images Not Displaying
**Problem:** Product images don't show

**Solution:**
1. Check file exists: `static/images/products/YOUR_IMAGE.jpg`
2. Verify database path: `SELECT image_url FROM products;`
3. Check path format: `/static/images/products/...`
4. Test direct access: `http://localhost:5000/static/images/products/chicken.jpg`

#### Login Issues
**Problem:** Can't log in with default credentials

**Solution:**
1. Run: `python add_required_users.py`
2. Check database: `SELECT * FROM users WHERE role='admin';`
3. Reset password if needed

#### Email Not Sending
**Problem:** Email notifications not working

**Solution:**
1. Check SMTP settings in `.env`
2. Verify email credentials
3. Enable "Less secure apps" or use app password
4. Check firewall/port 587

#### Port Already in Use
**Problem:** `Address already in use`

**Solution:**
```bash
# Find process using port 5000
netstat -ano | findstr :5000

# Kill process (Windows)
taskkill /PID <PID> /F

# Or use different port
python app.py --port 5001
```

### Getting Help

1. Check documentation in `docs/` folder
2. Review error logs
3. Check database for data integrity
4. Verify all dependencies installed
5. Test with default configuration

---

## 🤝 Contributing

### Development Setup

1. Fork the repository
2. Create feature branch: `git checkout -b feature-name`
3. Make changes
4. Test thoroughly
5. Commit: `git commit -m "Add feature"`
6. Push: `git push origin feature-name`
7. Create Pull Request

### Code Style
- Follow PEP 8 for Python
- Use meaningful variable names
- Add comments for complex logic
- Write docstrings for functions
- Keep functions focused and small

### Testing Requirements
- Test all new features
- Ensure existing tests pass
- Add tests for bug fixes
- Test on multiple browsers

---

## 📄 License

This project is developed for Sepik Fresh as part of an academic project.

**Copyright © 2026 Sepik Fresh. All rights reserved.**

---

## 👨‍💻 Development Team

- **Project:** Sepik Fresh Order Tracking System
- **Institution:** [Your Institution]
- **Course:** Object-Oriented Programming
- **Year:** 2026

---

## 📞 Support

For issues, questions, or support:

1. Check documentation in `docs/` folder
2. Review troubleshooting section
3. Check existing issues
4. Contact development team

---

## 🎉 Acknowledgments

- Flask framework and community
- Font Awesome for icons
- Unsplash/Pexels for stock images
- All contributors and testers

---

## 📊 Project Status

**Version:** 1.0  
**Status:** ✅ Production Ready  
**Last Updated:** April 2026

### Recent Updates
- ✅ Product images feature
- ✅ Home page slideshow
- ✅ Email notifications
- ✅ CSV export functionality
- ✅ User management
- ✅ Responsive design
- ✅ AI-powered alerts

---

## 🗺️ Roadmap

### Planned Features
- [ ] SMS notifications
- [ ] Payment integration
- [ ] Mobile app
- [ ] Advanced analytics
- [ ] Multi-language support
- [ ] API for third-party integration

---

**Made with ❤️ for Sepik Fresh**
