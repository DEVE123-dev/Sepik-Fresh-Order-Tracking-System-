@echo off
REM ============================================
REM Sepik Fresh - Automated Installation Script
REM For Windows Systems
REM ============================================

echo.
echo ================================================
echo   Sepik Fresh - Dependency Installation
echo ================================================
echo.

REM Check if Python is installed (try py first, then python)
py --version >nul 2>&1
if errorlevel 1 (
    python --version >nul 2>&1
    if errorlevel 1 (
        echo ERROR: Python is not installed or not in PATH
        echo Please install Python from https://www.python.org/
        pause
        exit /b 1
    )
    set PYTHON_CMD=python
) else (
    set PYTHON_CMD=py
)

echo [1/3] Python detected successfully
echo.

REM Check if pip is available
%PYTHON_CMD% -m pip --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: pip is not available
    echo Please reinstall Python with pip included
    pause
    exit /b 1
)

echo [2/3] pip detected successfully
echo.

REM Install dependencies
echo [3/3] Installing dependencies from requirements.txt...
echo.
%PYTHON_CMD% -m pip install -r requirements.txt

if errorlevel 1 (
    echo.
    echo ERROR: Failed to install dependencies
    pause
    exit /b 1
)

echo.
echo ================================================
echo   Installation Complete!
echo ================================================
echo.
echo Next steps:
echo   1. Make sure XAMPP is running (MySQL started)
echo   2. Run: python setup.py
echo   3. Run: python app.py
echo   4. Open: http://127.0.0.1:5000
echo.
pause
