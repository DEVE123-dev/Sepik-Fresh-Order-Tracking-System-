# ============================================
# Sepik Fresh Tracking System - Deployment Script
# ============================================
# This script automates the deployment of the Sepik Fresh application
# Author: Sepik Fresh Development Team
# Date: April 2026
# ============================================

Write-Host "============================================" -ForegroundColor Green
Write-Host "  Sepik Fresh Tracking System Deployment" -ForegroundColor Green
Write-Host "============================================" -ForegroundColor Green
Write-Host ""

# Check if Python is installed
Write-Host "[1/7] Checking Python installation..." -ForegroundColor Cyan
try {
    $pythonVersion = python --version 2>&1
    Write-Host "  ✓ Python found: $pythonVersion" -ForegroundColor Green
} catch {
    Write-Host "  ✗ Python not found! Please install Python 3.8 or higher." -ForegroundColor Red
    Write-Host "  Download from: https://www.python.org/downloads/" -ForegroundColor Yellow
    exit 1
}

# Check if pip is installed
Write-Host "[2/7] Checking pip installation..." -ForegroundColor Cyan
try {
    $pipVersion = pip --version 2>&1
    Write-Host "  ✓ pip found: $pipVersion" -ForegroundColor Green
} catch {
    Write-Host "  ✗ pip not found! Please install pip." -ForegroundColor Red
    exit 1
}

# Create virtual environment if it doesn't exist
Write-Host "[3/7] Setting up virtual environment..." -ForegroundColor Cyan
if (Test-Path "venv") {
    Write-Host "  ✓ Virtual environment already exists" -ForegroundColor Green
} else {
    Write-Host "  Creating virtual environment..." -ForegroundColor Yellow
    python -m venv venv
    Write-Host "  ✓ Virtual environment created" -ForegroundColor Green
}

# Activate virtual environment
Write-Host "[4/7] Activating virtual environment..." -ForegroundColor Cyan
& .\venv\Scripts\Activate.ps1
Write-Host "  ✓ Virtual environment activated" -ForegroundColor Green

# Install dependencies
Write-Host "[5/7] Installing dependencies..." -ForegroundColor Cyan
pip install -r requirements.txt --quiet
if ($LASTEXITCODE -eq 0) {
    Write-Host "  ✓ Dependencies installed successfully" -ForegroundColor Green
} else {
    Write-Host "  ✗ Failed to install dependencies" -ForegroundColor Red
    exit 1
}

# Check MySQL/MariaDB connection
Write-Host "[6/7] Checking database connection..." -ForegroundColor Cyan
Write-Host "  Please ensure MySQL/MariaDB is running" -ForegroundColor Yellow
Write-Host "  Default credentials:" -ForegroundColor Yellow
Write-Host "    - Username: root" -ForegroundColor Yellow
Write-Host "    - Password: (none)" -ForegroundColor Yellow
Write-Host "    - Database: sepik_database" -ForegroundColor Yellow
Write-Host ""
Write-Host "  Import database using phpMyAdmin or MySQL command:" -ForegroundColor Yellow
Write-Host "    mysql -u root sepik_database < database/database.sql" -ForegroundColor Cyan
Write-Host ""

# Add required users
Write-Host "[7/7] Setting up required users..." -ForegroundColor Cyan
Write-Host "  Creating admin and basic users with password: Pass@2026!" -ForegroundColor Yellow
python add_required_users.py
if ($LASTEXITCODE -eq 0) {
    Write-Host "  ✓ Required users created successfully" -ForegroundColor Green
} else {
    Write-Host "  ⚠ User setup completed (users may already exist)" -ForegroundColor Yellow
}

Write-Host ""
Write-Host "============================================" -ForegroundColor Green
Write-Host "  Deployment Complete!" -ForegroundColor Green
Write-Host "============================================" -ForegroundColor Green
Write-Host ""
Write-Host "To start the application:" -ForegroundColor Cyan
Write-Host "  python app.py" -ForegroundColor Yellow
Write-Host ""
Write-Host "Or use Gunicorn (production):" -ForegroundColor Cyan
Write-Host "  gunicorn -c gunicorn_config.py wsgi:app" -ForegroundColor Yellow
Write-Host ""
Write-Host "Access the application at:" -ForegroundColor Cyan
Write-Host "  http://localhost:5000" -ForegroundColor Yellow
Write-Host ""
Write-Host "Login credentials:" -ForegroundColor Cyan
Write-Host "  Admin: username='admin', password='Pass@2026!'" -ForegroundColor Yellow
Write-Host "  Basic: username='basic', password='Pass@2026!'" -ForegroundColor Yellow
Write-Host ""
Write-Host "============================================" -ForegroundColor Green
Write-Host ""

# Ask if user wants to start the application
$response = Read-Host "Do you want to start the application now? (Y/N)"
if ($response -eq 'Y' -or $response -eq 'y') {
    Write-Host ""
    Write-Host "Starting Sepik Fresh application..." -ForegroundColor Green
    Write-Host "Press Ctrl+C to stop the server" -ForegroundColor Yellow
    Write-Host ""
    python app.py
} else {
    Write-Host ""
    Write-Host "You can start the application later by running:" -ForegroundColor Cyan
    Write-Host "  python app.py" -ForegroundColor Yellow
    Write-Host ""
}
