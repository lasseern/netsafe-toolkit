# All-in-One Net Safe - Portable Python USB Version

This guide explains how to create a fully portable version with embedded Python.

## 📦 What You Need

1. **WinPython** (for Windows) - Portable Python distribution
2. **All tools pre-installed** in the tools directory
3. **Embedded Python launcher** scripts

## 🚀 Creating Portable USB Version

### Step 1: Download Portable Python

#### For Windows:
1. Download WinPython from: https://winpython.github.io/
2. Choose **WinPython 3.11.x** (or latest 3.x)
3. Download the "dot" version (portable, no installation)
4. Extract to USB stick root: `USB:\WPy64-3xxx`

#### For Linux (Portable):
1. Download Python portable build or use system Python
2. Create virtual environment on USB

### Step 2: Set Up Directory Structure

```
USB Stick Root/
├── WPy64-3xxx/              # Windows Portable Python
│   ├── python-3.x.x.amd64/
│   └── scripts/
├── AllInOneNetSafe/          # Your app
│   ├── main.py
│   ├── modules/
│   ├── tools/                # Pre-installed tools
│   │   ├── nipe/
│   │   ├── kalitorify/
│   │   ├── hakrawler/
│   │   ├── TorBot/
│   │   ├── BruteShark/
│   │   ├── PC-information/
│   │   └── DiskTest/
│   ├── venv/                 # Virtual environment
│   └── data/
├── START_WINDOWS.bat         # Windows launcher
├── START_LINUX.sh            # Linux launcher
└── README_USB.txt            # Instructions

```

### Step 3: Install All Dependencies

On your development machine:

```bash
cd AllInOneNetSafe
pip install -r requirements.txt --target=./lib
```

This installs all dependencies locally in the project.

### Step 4: Pre-Install All Tools

Run this script to pre-install everything:

```python
# pre_install_tools.py
import os
import subprocess

tools = {
    "nipe": "https://github.com/htrgouvea/nipe",
    "kalitorify": "https://github.com/brainfucksec/kalitorify",
    "hakrawler": "https://github.com/hakluke/hakrawler",
    "TorBot": "https://github.com/DedSecInside/TorBot",
    "BruteShark": "https://github.com/odedshimon/BruteShark",
    "PC-information": "https://github.com/nkhitrov/PC-information",
    "DiskTest": "https://github.com/maxim-saplin/NetCoreStorageSpeedTest"
}

tools_dir = "tools"
os.makedirs(tools_dir, exist_ok=True)

for name, url in tools.items():
    print(f"Cloning {name}...")
    subprocess.run(["git", "clone", url, os.path.join(tools_dir, name)])

print("All tools pre-installed!")
```

### Step 5: Create Portable Launchers

#### Windows: `START_WINDOWS.bat`

```batch
@echo off
echo ================================================
echo  All-in-One Net Safe - Portable USB Version
echo ================================================
echo.

REM Get USB drive letter
set "USB_DRIVE=%~d0"
set "APP_DIR=%~dp0AllInOneNetSafe"
set "PYTHON_DIR=%USB_DRIVE%\WPy64-3xxx\python-3.x.x.amd64"

echo USB Drive: %USB_DRIVE%
echo App Directory: %APP_DIR%
echo Python Directory: %PYTHON_DIR%
echo.

REM Check if Portable Python exists
if not exist "%PYTHON_DIR%\python.exe" (
    echo [ERROR] Portable Python not found!
    echo Please extract WinPython to: %USB_DRIVE%\WPy64-3xxx\
    echo Download from: https://winpython.github.io/
    pause
    exit /b 1
)

REM Add Python to PATH for this session only
set "PATH=%PYTHON_DIR%;%PYTHON_DIR%\Scripts;%PATH%"
set "PYTHONPATH=%APP_DIR%;%APP_DIR%\lib"

echo [OK] Python found: %PYTHON_DIR%\python.exe
python --version
echo.

REM Check/Install dependencies
echo Checking dependencies...
"%PYTHON_DIR%\python.exe" -m pip install --quiet --target="%APP_DIR%\lib" customtkinter psutil requests networkx matplotlib

REM Change to app directory
cd /d "%APP_DIR%"

echo.
echo Starting All-in-One Net Safe...
echo ================================================
echo.

REM Run the application
"%PYTHON_DIR%\python.exe" main.py

if %ERRORLEVEL% NEQ 0 (
    echo.
    echo [ERROR] Application crashed!
    pause
)
```

#### Linux: `START_LINUX.sh`

```bash
#!/bin/bash

echo "================================================"
echo " All-in-One Net Safe - Portable USB Version"
echo "================================================"
echo

# Get USB mount point
USB_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
APP_DIR="$USB_DIR/AllInOneNetSafe"
VENV_DIR="$APP_DIR/venv"

echo "USB Directory: $USB_DIR"
echo "App Directory: $APP_DIR"
echo

# Check for Python 3
if ! command -v python3 &> /dev/null; then
    echo "[ERROR] Python 3 not found!"
    echo "Please install Python 3.8 or higher"
    read -p "Press Enter to exit..."
    exit 1
fi

echo "[OK] Python found: $(which python3)"
python3 --version
echo

# Create virtual environment if it doesn't exist
if [ ! -d "$VENV_DIR" ]; then
    echo "Creating virtual environment..."
    python3 -m venv "$VENV_DIR"
fi

# Activate virtual environment
source "$VENV_DIR/bin/activate"

# Install dependencies
echo "Checking dependencies..."
pip install --quiet -r "$APP_DIR/requirements.txt"

# Change to app directory
cd "$APP_DIR"

echo
echo "Starting All-in-One Net Safe..."
echo "================================================"
echo

# Run the application
python main.py

if [ $? -ne 0 ]; then
    echo
    echo "[ERROR] Application crashed!"
    read -p "Press Enter to exit..."
fi

deactivate
```

### Step 6: Create README_USB.txt

```
==============================================================
  All-in-One Net Safe - Portable USB Version
==============================================================

QUICK START:

Windows:
  1. Double-click START_WINDOWS.bat
  2. First time: Downloads WinPython if needed
  3. Launches application

Linux:
  1. Open terminal in USB root
  2. chmod +x START_LINUX.sh
  3. ./START_LINUX.sh
  4. Launches application

==============================================================
PRE-INSTALLED TOOLS:
==============================================================

✓ Nipe - Tor routing
✓ Kalitorify - Transparent proxy
✓ Hakrawler - Web crawler
✓ TorBot - Dark web OSINT
✓ NetExec - Network pentesting
✓ NetworkX - Visualization
✓ PC-information - System info
✓ CrossPlatformDiskTest - Disk benchmark
✓ BruteShark - Network forensics

All tools are ready to use without installation!

==============================================================
REQUIREMENTS:
==============================================================

Windows:
  - WinPython portable (included)
  - Administrator rights for some tools

Linux:
  - Python 3.8+ (system)
  - sudo access for Tor tools

==============================================================
SUPPORT:
==============================================================

Documentation: AllInOneNetSafe/README.md
License: AllInOneNetSafe/LICENSE
Issues: GitHub repository

==============================================================
```

## 🎯 Benefits of Portable Version

✅ **No Installation Required** - Run from any USB stick
✅ **All Tools Pre-installed** - Ready to use immediately
✅ **Portable Python Included** - No system Python needed (Windows)
✅ **Cross-Platform** - Works on Windows and Linux
✅ **Self-Contained** - Everything in one place
✅ **Privacy-Focused** - Leave no traces on host system
✅ **Field-Ready** - Perfect for penetration testing

## ⚠️ Important Notes

1. **USB Speed**: Use USB 3.0+ for better performance
2. **Disk Space**: ~2-3 GB required for full installation
3. **Admin Rights**: Some tools require elevated privileges
4. **Antivirus**: May flag security tools - add exclusions
5. **Legal**: Only use on authorized systems

## 📝 License

Portable version follows same license as main application.
See LICENSE file for details.
