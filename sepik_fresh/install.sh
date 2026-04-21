#!/bin/bash
# ============================================
# Sepik Fresh - Automated Installation Script
# For Linux/Mac Systems
# ============================================

echo ""
echo "================================================"
echo "  Sepik Fresh - Dependency Installation"
echo "================================================"
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "ERROR: Python 3 is not installed"
    echo "Please install Python 3 from https://www.python.org/"
    exit 1
fi

echo "[1/3] Python detected successfully"
echo ""

# Check if pip is available
if ! python3 -m pip --version &> /dev/null; then
    echo "ERROR: pip is not available"
    echo "Please install pip: sudo apt install python3-pip"
    exit 1
fi

echo "[2/3] pip detected successfully"
echo ""

# Install dependencies
echo "[3/3] Installing dependencies from requirements.txt..."
echo ""
python3 -m pip install -r requirements.txt

if [ $? -ne 0 ]; then
    echo ""
    echo "ERROR: Failed to install dependencies"
    exit 1
fi

echo ""
echo "================================================"
echo "  Installation Complete!"
echo "================================================"
echo ""
echo "Next steps:"
echo "  1. Make sure MySQL is running"
echo "  2. Run: python3 setup.py"
echo "  3. Run: python3 app.py"
echo "  4. Open: http://127.0.0.1:5000"
echo ""
