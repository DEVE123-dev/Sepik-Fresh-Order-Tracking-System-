# Sepik Fresh - Installation Guide

This guide will help you set up the Sepik Fresh Order Tracking System on a new computer.

---

## Prerequisites

Before installing, make sure you have:

1. **Python 3.8 or higher**
   - Download from: https://www.python.org/downloads/
   - During installation, check "Add Python to PATH"

2. **XAMPP** (for MySQL database)
   - Download from: https://www.apachefriends.org/
   - Install and start Apache + MySQL services

3. **Git** (optional - for cloning the repository)
   - Download from: https://git-scm.com/

---

## Installation Methods

### Method 1: Automated Installation (Recommended)

#### For Windows:
```bash
# Navigate to the project folder
cd sepik_fresh

# Run the installation script
install.bat
```

#### For Linux/Mac:
```bash
# Navigate to the project folder
cd sepik_fresh

# Make the script executable
chmod +x install.sh

# Run the installation script
./install.sh
```

The script will:
- Check if Python and pip are installed
- Install all required dependencies from `requirements.txt`
- Show next steps

---

### Method 2: Manual Installation

#### Step 1: Install Python Dependencies

```bash
# Navigate to the project folder
cd sepik_fresh

# Install dependencies using pip
python -m pip install -r requirements.txt
```

This will install:
- `flask>=3.0.0` - Web framework
- `mysql-connector-python>=8.0.0` - MySQL database connector
- `bcrypt>=4.0.0` - Password hashing
- `python-dotenv>=1.0.0` - Environment variable management
- `pytest>=7.4.0` - Testing framework (optional)
- `pytest-flask>=1.2.0` - Flask testing utilities (optional)

#### Step 2: Verify Installation

```bash
python -m pip list
```

You should see all the packages listed above.

---

## Database Setup

After installing dependencies, set up the database:

### Step 1: Start XAMPP
1. Open XAMPP Control Panel
2. Start **Apache** service
3. Start **MySQL** service

### Step 2: Run Database Setup Script

```bash
# Navigate to the project folder
cd sepik_fresh

# Run the setup script
python setup.py
```

This will:
- Create the `sepik_database` database
- Create all required tables
- Insert sample data and test accounts

---

## Running the Application

### Start the Flask Application

```bash
# Navigate to the project folder
cd sepik_fresh

# Run the application
python app.py
```

You should see:
```
 * Running on http://127.0.0.1:5000
 * Press CTRL+C to quit
```

### Access the Application

Open your web browser and go to:
```
http://127.0.0.1:5000
```

---

## Test Accounts

Use these accounts to test the system:

| Role | Email | Password |
|------|-------|----------|
| **Administrator** | admin@sepikfresh.pg | admin123 |
| **Customer** | isho@sepikfresh.pg | password123 |
| **Delivery Staff** | staff@sepikfresh.pg | staff123 |

---

## Troubleshooting

### Problem: "Python is not recognized"
**Solution:** 
- Reinstall Python and check "Add Python to PATH"
- Or manually add Python to system PATH

### Problem: "pip is not recognized"
**Solution:**
```bash
python -m ensurepip --upgrade
```

### Problem: "Could not connect to MySQL"
**Solution:**
- Make sure XAMPP is running
- Check that MySQL service is started in XAMPP Control Panel
- Verify MySQL is running on port 3306

### Problem: "Access denied for user 'root'"
**Solution:**
- Check MySQL password in `config.py`
- Default XAMPP password is empty ('')
- Update `config.py` if you changed the MySQL password

### Problem: "Module not found"
**Solution:**
```bash
# Reinstall all dependencies
python -m pip install -r requirements.txt --force-reinstall
```

### Problem: "Port 5000 already in use"
**Solution:**
- Change the port in `app.py`:
```python
if __name__ == '__main__':
    app.run(debug=True, port=5001)  # Use port 5001 instead
```

---

## Project Structure

```
sepik_fresh/
├── app.py                  # Main application file
├── config.py               # Configuration settings
├── models.py               # Database models
├── agents.py               # Background monitoring
├── email_utils.py          # Email notifications
├── requirements.txt        # Python dependencies
├── setup.py                # Database setup script
├── install.bat             # Windows installation script
├── install.sh              # Linux/Mac installation script
├── database/
│   └── sepik_database.sql  # Database schema and data
├── templates/              # HTML templates
├── static/                 # CSS, JS, images
└── tests/                  # Unit tests
```

---

## Next Steps After Installation

1. **Explore the System:**
   - Login as admin to manage products and orders
   - Login as customer to place and track orders
   - Login as staff to update delivery status

2. **Customize Configuration:**
   - Edit `config.py` for database settings
   - Edit `.env.example` and rename to `.env` for email settings

3. **Run Tests (Optional):**
   ```bash
   python run_tests.py
   ```

4. **Deploy to Production:**
   - See `README.md` for deployment instructions
   - Use `gunicorn_config.py` for production server

---

## Support

For issues or questions:
- Check the main `README.md` file
- Review the troubleshooting section above
- Check XAMPP logs in `xampp/mysql/data/`

---

## System Requirements

- **Operating System:** Windows 10/11, Linux, macOS
- **Python:** 3.8 or higher
- **RAM:** 2GB minimum, 4GB recommended
- **Disk Space:** 500MB for application and database
- **Browser:** Chrome, Firefox, Edge, Safari (latest versions)

---

## Quick Reference Commands

```bash
# Install dependencies
python -m pip install -r requirements.txt

# Setup database
python setup.py

# Run application
python app.py

# Run tests
python run_tests.py

# Check installed packages
python -m pip list

# Update a package
python -m pip install --upgrade flask
```

---

**Installation Complete!** 🎉

You're now ready to use the Sepik Fresh Order Tracking System.
