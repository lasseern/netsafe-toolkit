#!/bin/bash
# ================================================
#  All-in-One Net Safe - Portable USB Launcher
#  Supports portable and system Python
# ================================================

echo ""
echo "================================================"
echo " All-in-One Net Safe - USB Edition"
echo "================================================"
echo ""

# Get USB/app directory
USB_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
APP_DIR="$USB_DIR"
VENV_DIR="$APP_DIR/venv"

echo "USB Directory: $USB_DIR"
echo "App Directory: $APP_DIR"
echo ""

# === Check for Python 3 ===
if ! command -v python3 &> /dev/null; then
    echo "================================================"
    echo " ERROR: Python 3 Not Found!"
    echo "================================================"
    echo ""
    echo "Please install Python 3.8 or higher:"
    echo ""
    echo "Ubuntu/Debian:"
    echo "  sudo apt update"
    echo "  sudo apt install python3 python3-pip python3-venv"
    echo ""
    echo "Fedora/RHEL:"
    echo "  sudo dnf install python3 python3-pip"
    echo ""
    echo "Arch:"
    echo "  sudo pacman -S python python-pip"
    echo ""
    read -p "Press Enter to exit..."
    exit 1
fi

echo "[OK] Python found: $(which python3)"
python3 --version
echo ""

# === Create/Use Virtual Environment ===
if [ ! -d "$VENV_DIR" ]; then
    echo "Creating virtual environment..."
    python3 -m venv "$VENV_DIR"
    if [ $? -ne 0 ]; then
        echo "[ERROR] Failed to create virtual environment!"
        read -p "Press Enter to exit..."
        exit 1
    fi
    echo "[OK] Virtual environment created"
fi

echo "Activating virtual environment..."
source "$VENV_DIR/bin/activate"

if [ $? -ne 0 ]; then
    echo "[ERROR] Failed to activate virtual environment!"
    read -p "Press Enter to exit..."
    exit 1
fi

echo "[OK] Virtual environment activated"
echo ""

# === Install Dependencies ===
echo "================================================"
echo " Installing Dependencies"
echo "================================================"
echo ""
echo "This may take a few minutes on first run..."
echo ""

pip install --quiet --upgrade pip
pip install --quiet -r "$APP_DIR/requirements.txt"

if [ $? -ne 0 ]; then
    echo ""
    echo "[WARNING] Some dependencies may have failed."
    echo "The application will attempt to run anyway..."
    echo ""
else
    echo "[OK] All dependencies installed"
fi

echo ""

# === Launch Application ===
echo "================================================"
echo " Starting All-in-One Net Safe"
echo "================================================"
echo ""
echo " 10 Security Tools Ready:"
echo " [1] Tor Routing (Nipe)"
echo " [2] Transparent Proxy (Kalitorify)"
echo " [3] Web Crawler (Hakrawler)"
echo " [4] Dark Web OSINT (TorBot)"
echo " [5] Network Pentesting (NetExec)"
echo " [6] Network Forensics (BruteShark)"
echo " [7] PC Information"
echo " [8] Disk Benchmark"
echo " [9] Network Visualizer"
echo " [10] System Tools"
echo ""
echo "================================================"
echo ""

cd "$APP_DIR"
export PYTHONPATH="$APP_DIR:$APP_DIR/lib"
export NETSAFE_USB_MODE=1

python main.py

if [ $? -ne 0 ]; then
    echo ""
    echo "================================================"
    echo " Application Error"
    echo "================================================"
    echo ""
    echo "Check logs in: $APP_DIR/logs/"
    echo ""
    read -p "Press Enter to exit..."
fi

deactivate
