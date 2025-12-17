==============================================================
  ALL-IN-ONE NET SAFE - PORTABLE USB EDITION
==============================================================

VERSION: 3.0 (English)
UPDATED: December 17, 2025

==============================================================
QUICK START
==============================================================

WINDOWS:
  Double-click: START_USB_WINDOWS.bat
  
  First time:
  - Will detect Python (system or portable)
  - Installs dependencies automatically
  - Launches application
  
  Portable Python (optional):
  - Download WinPython from https://winpython.github.io/
  - Extract to USB:\WPy64-31\
  - Rerun START_USB_WINDOWS.bat

LINUX:
  1. Open terminal in USB root directory
  2. chmod +x START_USB_LINUX.sh
  3. ./START_USB_LINUX.sh
  
  First time:
  - Creates virtual environment
  - Installs dependencies
  - Launches application

==============================================================
PRE-INSTALLATION (OPTIONAL)
==============================================================

To pre-install all tools before copying to USB:

  python usb_preinstall.py

This will:
  ✓ Clone all GitHub repositories
  ✓ Download binary tools
  ✓ Set up directory structure
  ✓ Create necessary files

Benefits:
  - Faster first-time launch
  - Works offline (no internet needed on target PC)
  - All tools ready immediately

==============================================================
INTEGRATED SECURITY TOOLS (10 TOTAL)
==============================================================

[1] NIPE - Tor Network Routing
    License: MIT
    Purpose: Route all system traffic through Tor
    Platform: Linux, WSL
    Requires: Perl, Tor, sudo

[2] KALITORIFY - Transparent Proxy
    License: GPL-3.0
    Purpose: Transparent Tor proxy via iptables
    Platform: Kali Linux, Debian
    Requires: Tor, iptables, sudo

[3] HAKRAWLER - Web Crawler
    License: GPL-3.0
    Purpose: Fast web reconnaissance and link discovery
    Platform: Cross-platform
    Requires: Go (for building)

[4] TORBOT - Dark Web OSINT
    License: GPL-3.0
    Purpose: Scan and analyze .onion sites
    Platform: Cross-platform
    Requires: Python 3.9+, Tor (optional)

[5] NETEXEC - Network Pentesting
    License: BSD-2
    Purpose: Network service enumeration and exploitation
    Platform: Cross-platform
    Requires: pipx, Python 3.8+

[6] BRUTESHARK - Network Forensics
    License: GPL-3.0
    Purpose: PCAP analysis and credential extraction
    Platform: Windows, Linux
    Requires: Npcap (Win) or libpcap (Linux)

[7] PC-INFORMATION - System Info
    License: MIT
    Purpose: Hardware and software inventory
    Platform: Windows (full), Cross-platform (basic)
    Requires: PowerShell (Windows) or psutil (Python)

[8] DISK BENCHMARK - Storage Testing
    License: MIT
    Purpose: Measure disk read/write performance
    Platform: Cross-platform
    Requires: Python 3.8+

[9] NETWORKX - Network Visualization
    License: BSD-3
    Purpose: Interactive network graphs
    Platform: Cross-platform
    Requires: matplotlib

[10] NETWORK VISUALIZER
     Purpose: Visualize crawler and OSINT results
     Platform: Cross-platform
     Requires: NetworkX, matplotlib

==============================================================
NEW FEATURES IN VERSION 3.0
==============================================================

✨ ENGLISH INTERFACE
   - Entire application translated to English
   - All menus, buttons, and messages in English
   - English documentation

✨ TOOLTIPS EVERYWHERE
   - Hover over any button to see what it does
   - Detailed explanations for each tool
   - Helpful hints and tips

✨ EMBEDDED PYTHON SUPPORT
   - Run from USB with WinPython (no system install)
   - Portable Python included (optional)
   - No traces left on host system

✨ PRE-INSTALLED TOOLS
   - Optional pre-install script
   - All tools ready to use
   - Faster startup time

==============================================================
SYSTEM REQUIREMENTS
==============================================================

MINIMUM:
  - Windows 10/11 OR Linux (Ubuntu, Kali, Debian, etc.)
  - Python 3.8 or higher
  - 2 GB free disk space (for tools)
  - USB 3.0 stick (recommended)
  - Internet connection (first run only)

RECOMMENDED:
  - 4 GB RAM
  - USB 3.0 or faster
  - Administrator/sudo access
  - Git installed (for tool cloning)

OPTIONAL:
  - WinPython portable (Windows)
  - Go compiler (for Hakrawler)
  - Tor Browser (for dark web tools)

==============================================================
FIRST TIME SETUP
==============================================================

1. COPY TO USB:
   - Copy entire "All in one net safe" folder to USB
   - Maintain folder structure
   - Do not rename folders

2. WINDOWS SETUP:
   a) Install Python 3.8+ from python.org, OR
   b) Download WinPython and extract to USB:\WPy64-31\

3. LINUX SETUP:
   a) Install Python 3.8+
      Ubuntu/Debian: sudo apt install python3 python3-pip python3-venv
      Fedora: sudo dnf install python3 python3-pip
      Arch: sudo pacman -S python python-pip

4. OPTIONAL - PRE-INSTALL TOOLS:
   python usb_preinstall.py

5. RUN:
   Windows: START_USB_WINDOWS.bat
   Linux: ./START_USB_LINUX.sh

==============================================================
USING THE APPLICATION
==============================================================

MAIN WINDOW:
  - 11 tabs for different tools
  - Modern dark/light theme
  - Real-time status updates
  - Comprehensive logging

INSTALLING TOOLS:
  - Click "Install" button in each tab
  - Wait for download and setup
  - Tool status shown in tab
  - Install once, use many times

TOOLTIPS:
  - Hover mouse over any button
  - Read what the tool does
  - Get usage hints
  - Learn keyboard shortcuts

COMMON TASKS:
  
  Anonymous Browsing:
    1. Go to "Tor" tab
    2. Click "Install Nipe" (first time)
    3. Click "Start Tor"
    4. Your IP is now anonymous

  Web Reconnaissance:
    1. Go to "Crawler" tab
    2. Click "Install Hakrawler" (first time)
    3. Enter target URL
    4. Click "Start Crawl"
    5. View results and save

  Network Forensics:
    1. Go to "BruteShark" tab
    2. Click "Install" (first time)
    3. Click "Browse" to select PCAP file
    4. Select analysis modules
    5. Click "Analyze PCAP"

  System Information:
    1. Go to "PC Info" tab
    2. Click "Basic Info" (cross-platform)
       OR "Full System Scan" (Windows)
    3. View hardware details

==============================================================
TROUBLESHOOTING
==============================================================

"Python not found":
  - Install Python 3.8+ from python.org
  - Check "Add Python to PATH" during install
  - Restart terminal/command prompt

"Permission denied" (Linux):
  - chmod +x START_USB_LINUX.sh
  - Some tools require: sudo ./START_USB_LINUX.sh

"Dependencies failed":
  - Check internet connection
  - Run: pip install -r requirements.txt
  - Try again

"Tool install failed":
  - Check internet connection
  - Check antivirus (may block security tools)
  - Try installing manually via GUI

"Slow USB performance":
  - Use USB 3.0 or faster
  - Avoid running from compressed drives
  - Consider pre-installing tools

==============================================================
SECURITY & LEGAL
==============================================================

⚠️  IMPORTANT:
  - Only use on systems you own or have permission to test
  - Some tools require administrator/sudo access
  - Security tools may trigger antivirus warnings
  - Tor routing affects entire system

✅ LEGAL USE:
  - Authorized penetration testing
  - Security research
  - Privacy protection
  - Educational purposes
  - Network analysis

❌ ILLEGAL USE:
  - Unauthorized access
  - Network attacks
  - Data theft
  - Any illegal activity

By using this software, you agree to use it responsibly
and in compliance with all applicable laws.

==============================================================
PORTABLE PRIVACY
==============================================================

Advantages:
  ✓ No system installation required
  ✓ Leave no traces on host computer
  ✓ Works on multiple machines
  ✓ All data stored on USB
  ✓ Easy to update and maintain

Best Practices:
  - Use encrypted USB stick
  - Always eject properly
  - Keep USB in safe location
  - Regular backups
  - Update tools regularly

==============================================================
SUPPORT & RESOURCES
==============================================================

Documentation:
  - README.md - Main documentation
  - PORTABLE_PYTHON_GUIDE.md - Portable Python setup
  - FEATURES.md - Feature overview
  - CHANGELOG.md - Version history
  - LICENSE - Legal information

Logs:
  - Application logs: logs/netsafe.log
  - Check for errors and warnings
  - Useful for troubleshooting

GitHub:
  - Report issues
  - Request features
  - Contribute code
  - View source

==============================================================
CREDITS
==============================================================

Integrated Projects:
  - Nipe: @htrgouvea
  - Kalitorify: @brainfucksec
  - Hakrawler: @hakluke
  - TorBot: @DedSecInside
  - NetExec: @Pennyw0rth
  - BruteShark: @odedshimon
  - PC-information: @nkhitrov
  - CrossPlatformDiskTest: @maxim-saplin
  - NetworkX: NetworkX Team
  - CustomTkinter: @TomSchimansky

Special Thanks:
  - The Tor Project
  - All open source contributors
  - Security research community

==============================================================
LICENSE
==============================================================

Main Application: MIT License
Integrated Tools: Various (see LICENSE file)

See LICENSE file for complete license information and
attributions for all integrated projects.

==============================================================
END OF USB GUIDE
==============================================================

For latest version and updates:
https://github.com/[your-repo]/all-in-one-net-safe

Last updated: December 17, 2025
Version: 3.0 (English Edition with Tooltips)
