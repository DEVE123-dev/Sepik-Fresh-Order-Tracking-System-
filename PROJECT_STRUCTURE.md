# 📂 Project Structure

## Overview

This document explains the organization of the Sepik Fresh project files.

---

## 📁 Root Directory

```
sepik-fresh/
│
├── README.md                    # Main project documentation
├── DOCUMENTATION.md            # Documentation guide
├── PROJECT_STRUCTURE.md        # This file
│
├── docs/                       # All markdown documentation (22 files)
│   ├── INDEX.md               # Documentation index
│   ├── QUICK_START.md
│   ├── INSTALLATION_GUIDE.md
│   ├── PRODUCT_IMAGES_FEATURE.md
│   └── ... (see docs/INDEX.md for full list)
│
├── sepik_fresh/               # Main application folder
│   ├── app.py                # Main Flask application
│   ├── models.py             # Database models (OOP)
│   ├── config.py             # Configuration
│   ├── agents.py             # AI monitoring agents
│   ├── email_utils.py        # Email functionality
│   ├── requirements.txt      # Python dependencies
│   │
│   ├── START_HERE.txt        # Quick image setup guide
│   ├── IMAGE_PATHS_REFERENCE.txt
│   ├── FOLDER_STRUCTURE_GUIDE.txt
│   ├── QUICK_START_IMAGES.txt
│   ├── IMAGE_SRC_EXAMPLES.txt
│   ├── FEATURE_FLOW_DIAGRAM.txt
│   │
│   ├── database/             # Database files
│   │   ├── sepik_database.sql
│   │   ├── updates.sql
│   │   └── add_product_images.sql
│   │
│   ├── static/               # Static assets
│   │   ├── css/
│   │   │   ├── main.css
│   │   │   ├── dashboard.css
│   │   │   └── login.css
│   │   ├── js/
│   │   │   ├── main.js
│   │   │   └── dashboard.js
│   │   └── images/
│   │       ├── logo.jpeg
│   │       ├── background.png
│   │       └── products/     # Product images go here
│   │
│   ├── templates/            # HTML templates
│   │   ├── home.html
│   │   ├── products.html
│   │   ├── order_new.html
│   │   ├── dashboard_admin.html
│   │   └── ... (30+ templates)
│   │
│   └── tests/                # Test files
│       ├── test_models.py
│       └── test_routes.py
│
└── out/                      # Build output (if any)
```

---

## 📖 Documentation Organization

### Root Level
- **README.md** - Main project documentation with everything you need
- **DOCUMENTATION.md** - Guide to finding documentation
- **PROJECT_STRUCTURE.md** - This file

### docs/ Folder
All `.md` documentation files organized by category:

**Setup & Installation:**
- QUICK_START.md
- INSTALLATION_GUIDE.md
- PASSWORD_SETUP_GUIDE.md

**Features:**
- PRODUCT_IMAGES_FEATURE.md
- ENHANCEMENTS_ADDED.md
- IMPLEMENTATION_COMPLETE.md

**Planning:**
- AGILE_PLANNING.md
- USER_STORIES.md
- UML_DIAGRAMS.md
- STAKEHOLDER_ANALYSIS.md

**Testing:**
- TESTING_CHECKLIST.md
- AGENT_TESTING_GUIDE.md

**Submission:**
- PROJECT_SUBMISSION_README.md
- SUBMISSION_CHECKLIST.md
- ASSIGNMENT_COMPLIANCE_REPORT.md

See **[docs/INDEX.md](docs/INDEX.md)** for complete list.

### sepik_fresh/ Quick Reference Files
Simple `.txt` files for quick reference:
- **START_HERE.txt** - Simplest setup guide
- **IMAGE_PATHS_REFERENCE.txt** - Image path quick reference
- **FOLDER_STRUCTURE_GUIDE.txt** - Folder structure guide
- **QUICK_START_IMAGES.txt** - Quick image setup
- **IMAGE_SRC_EXAMPLES.txt** - Template examples
- **FEATURE_FLOW_DIAGRAM.txt** - Feature flow diagrams

---

## 🎯 Where to Find What

### "How do I get started?"
→ **[README.md](README.md)** - Quick Start section

### "How do I add product images?"
→ **[sepik_fresh/START_HERE.txt](sepik_fresh/START_HERE.txt)**

### "Where's the detailed installation guide?"
→ **[docs/INSTALLATION_GUIDE.md](docs/INSTALLATION_GUIDE.md)**

### "What features are included?"
→ **[README.md](README.md)** - Features section

### "How do I test the system?"
→ **[docs/TESTING_CHECKLIST.md](docs/TESTING_CHECKLIST.md)**

### "Where are all the documentation files?"
→ **[docs/INDEX.md](docs/INDEX.md)**

---

## 🗂️ File Types

### Python Files (.py)
- `app.py` - Main application
- `models.py` - Database models
- `config.py` - Configuration
- `agents.py` - AI agents
- `email_utils.py` - Email utilities

### SQL Files (.sql)
- `sepik_database.sql` - Main database schema
- `updates.sql` - Database updates
- `add_product_images.sql` - Image column addition

### HTML Files (.html)
- All in `templates/` folder
- 30+ template files

### CSS Files (.css)
- `main.css` - Main styles
- `dashboard.css` - Dashboard styles
- `login.css` - Login page styles

### JavaScript Files (.js)
- `main.js` - Main scripts
- `dashboard.js` - Dashboard scripts

### Documentation Files
- `.md` files → `docs/` folder
- `.txt` files → `sepik_fresh/` folder (quick reference)

---

## 📝 Key Files

### Must Read
1. **README.md** - Start here
2. **sepik_fresh/START_HERE.txt** - Image setup
3. **docs/QUICK_START.md** - Quick start guide

### Configuration
1. **sepik_fresh/.env** - Environment variables (create from .env.example)
2. **sepik_fresh/config.py** - Application config

### Database
1. **sepik_fresh/database/sepik_database.sql** - Main schema
2. **sepik_fresh/database/updates.sql** - Updates
3. **sepik_fresh/database/add_product_images.sql** - Image support

---

## 🎨 Static Assets

### Images
- **Logo:** `static/images/logo.jpeg`
- **Background:** `static/images/background.png`
- **Products:** `static/images/products/` ← Add product images here

### Styles
- **Main:** `static/css/main.css`
- **Dashboard:** `static/css/dashboard.css`
- **Login:** `static/css/login.css`

### Scripts
- **Main:** `static/js/main.js`
- **Dashboard:** `static/js/dashboard.js`

---

## 🔍 Finding Files

### By Purpose

**Setup:**
- README.md
- docs/INSTALLATION_GUIDE.md
- sepik_fresh/START_HERE.txt

**Development:**
- sepik_fresh/app.py
- sepik_fresh/models.py
- sepik_fresh/templates/

**Styling:**
- sepik_fresh/static/css/

**Database:**
- sepik_fresh/database/

**Documentation:**
- docs/

**Testing:**
- sepik_fresh/tests/
- docs/TESTING_CHECKLIST.md

---

## 💡 Tips

1. **Start with README.md** - It has everything you need
2. **Use docs/INDEX.md** - To find specific documentation
3. **Quick reference?** - Check .txt files in sepik_fresh/
4. **Need help?** - Check DOCUMENTATION.md

---

**Last Updated:** April 2026
