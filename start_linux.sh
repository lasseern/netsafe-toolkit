#!/bin/bash
# Portable Launcher for Linux/Unix

echo "================================================"
echo "  All-in-One Net Safe - Portable Linux Launcher"
echo "================================================"
echo ""

# Få script directory
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd "$SCRIPT_DIR"

# Tjek om Python er installeret
if ! command -v python3 &> /dev/null; then
    echo "ERROR: Python 3 er ikke installeret!"
    echo ""
    echo "Installer Python 3:"
    echo "  Ubuntu/Debian: sudo apt install python3 python3-pip"
    echo "  Fedora/RHEL: sudo dnf install python3 python3-pip"
    echo "  Arch: sudo pacman -S python python-pip"
    exit 1
fi

echo "Python fundet: $(python3 --version)"
echo "Working directory: $SCRIPT_DIR"
echo ""

# Tjek om requirements er installeret
if ! python3 -c "import customtkinter" &> /dev/null; then
    echo "Installerer dependencies..."
    python3 -m pip install --user -r requirements.txt
    if [ $? -ne 0 ]; then
        echo ""
        echo "ERROR: Kunne ikke installere dependencies"
        exit 1
    fi
fi

echo ""
echo "Starting All-in-One Net Safe..."
echo ""

# Start programmet
python3 portable_launcher.py

if [ $? -ne 0 ]; then
    echo ""
    echo "Program afsluttet med fejl"
    read -p "Tryk Enter for at afslutte..."
fi
