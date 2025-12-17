# 🛡️ All-in-One Net Safe v3.0

A comprehensive security toolkit with 10 integrated tools for anonymous browsing, network reconnaissance, forensics analysis, and system diagnostics - all with an intuitive GUI and helpful tooltips.

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)
![Version](https://img.shields.io/badge/Version-3.0-orange.svg)

## ✨ What's New in v3.0

### 🌍 **English Interface**
- Complete English translation throughout
- All buttons, menus, and messages in English
- English documentation and guides

### 💡 **Interactive Tooltips**
- Hover over any button to see what it does
- Detailed explanations for each tool
- Usage hints and tips built-in
- No more guessing - instant help everywhere!

### 💾 **Portable Python Support**
- Run from USB with embedded WinPython
- No system Python installation required (Windows)
- True portable experience - leave no traces
- Works on any computer

### 📦 **Pre-Install Option**
- Optional script to pre-install all tools
- Faster startup on USB stick
- Works offline after initial setup
- Perfect for field work

## 🌟 Features

### 10 Integrated Security Tools

| # | Tool | Purpose | Platform | License |
|---|------|---------|----------|---------|
| 1 | 🔐 **Nipe** | Tor network routing | Linux, WSL | MIT |
| 2 | 🛡️ **Kalitorify** | Transparent proxy | Kali Linux | GPL-3.0 |
| 3 | 🕷️ **Hakrawler** | Web crawler | Cross-platform | GPL-3.0 |
| 4 | 🌑 **TorBot** | Dark web OSINT | Cross-platform | GPL-3.0 |
| 5 | ⚡ **NetExec** | Network pentesting | Cross-platform | BSD-2 |
| 6 | 🦈 **BruteShark** | Network forensics | Win/Linux | GPL-3.0 |
| 7 | 💻 **PC-Info** | System information | Cross-platform | MIT |
| 8 | 💾 **Disk Test** | Storage benchmark | Cross-platform | MIT |
| 9 | 📊 **Visualizer** | Network graphs | Cross-platform | BSD-3 |
| 10 | 🛠️ **System Tools** | Various utilities | Cross-platform | Various |

### Key Capabilities

- **Anonymous Browsing**: Route traffic through Tor network
- **Web Reconnaissance**: Discover links, subdomains, endpoints
- **Dark Web Intel**: Safely scan .onion sites
- **Network Analysis**: PCAP forensics and credential extraction
- **System Diagnostics**: Hardware info and disk benchmarking
- **Visualization**: Interactive network topology graphs
- **Portable Operation**: Run from USB stick, no installation

## 📋 System Requirements

### Minimum
- **OS**: Windows 10/11 or Linux (Ubuntu, Kali, Debian, Arch, etc.)
- **Python**: 3.8 or higher
- **RAM**: 4 GB
- **Disk**: 2-3 GB free space
- **Internet**: Required for tool installation

### Recommended
- **USB**: 3.0 or faster (for portable version)
- **Privileges**: Administrator/sudo access
- **Tools**: Git, Perl, Go (for some integrations)

### Optional
- WinPython portable (Windows USB version)
- Tor Browser (for dark web tools)
- Wireshark/Npcap (for network forensics)

## 🚀 Installation

### Method 1: Standard Installation

```bash
# Clone repository
git clone <your-repo-url>
cd "all in one net safe"

# Install Python dependencies
pip install -r requirements.txt

# Run application
python main.py
```

### Method 2: Portable USB Installation

#### Windows:
```batch
# 1. Copy entire folder to USB stick
# 2. (Optional) Download WinPython from https://winpython.github.io/
#    Extract to USB:\WPy64-31\
# 3. Double-click START_USB_WINDOWS.bat
```

#### Linux:
```bash
# 1. Copy entire folder to USB stick
# 2. Open terminal in USB directory
chmod +x START_USB_LINUX.sh
./START_USB_LINUX.sh
```

### Method 3: Pre-Installed USB Version

```bash
# Pre-install all tools before copying to USB
python usb_preinstall.py

# Then copy to USB and use launchers
```

## 📖 Quick Start Guide

### First Launch
1. Start application using method above
2. Modern GUI opens with 11 tabs
3. **Hover over buttons** to see tooltips
4. Install tools as needed via GUI

### Using Tooltips
- **Hover mouse** over any button
- **Read description** of what it does
- **Learn requirements** for each tool
- **Get usage hints** instantly

### Example: Anonymous Browsing

```
1. Go to "🔐 Tor" tab
2. Hover over buttons to learn what they do
3. Click "📥 Install Nipe" (first time only)
4. Click "▶️ Start Tor" to activate routing
5. Your IP is now anonymous via Tor network
6. Click "🔄 New Circuit" to change exit node
```

### Example: Web Reconnaissance

```
1. Go to "🕷️ Crawler" tab
2. Hover over "Install" to see what Hakrawler does
3. Click "📥 Install Hakrawler" (first time)
4. Enter target URL (e.g., https://example.com)
5. Set crawl depth (1-10)
6. Click "🚀 Start Crawl"
7. View discovered links in results
8. Optional: Visualize in "📊 Visualizer" tab
```

### Example: Network Forensics

```
1. Go to "🦈 BruteShark" tab
2. Read tooltips to understand capabilities
3. Click "📥 Install" (first time)
4. Click "📁 Browse" to select PCAP file
5. Select analysis modules (hover to learn about each):
   ✓ Credentials - Extract passwords
   ✓ Network Map - Build topology
   ✓ File Extraction - Carve files
   ✓ DNS - Extract queries
6. Click "🔍 Analyze PCAP"
7. Review extracted data
```

## 🎨 Interface Features

### 11 Tabs
1. **🔐 Tor** - Anonymous routing via Nipe
2. **🛡️ Kalitorify** - Transparent proxy
3. **🕷️ Crawler** - Web reconnaissance
4. **🌑 DarkWeb** - .onion site analysis
5. **⚡ NetExec** - Network pentesting
6. **📊 Visualizer** - Network graphs
7. **💻 PC Info** - System information
8. **💾 Disk Test** - Storage benchmarking
9. **🦈 BruteShark** - Network forensics
10. **⚙️ Settings** - Configuration
11. **ℹ️ About** - Information

### Modern UI
- Dark/Light/System themes
- Real-time status updates
- Progress indicators
- Comprehensive logging
- Responsive design

### Tooltip System
- **Every button** has a tooltip
- **Hover to learn** - no manual needed
- **Context-sensitive** help
- **Beginner-friendly** explanations

## 🛠️ Tool Details

### Tor Routing (Nipe)
- Route all traffic through Tor
- Change IP with new circuits
- IPv4/IPv6 support
- Requires: Perl, Tor, sudo

### Transparent Proxy (Kalitorify)
- Force all traffic through Tor
- Iptables-based routing
- Kali Linux specialized
- Requires: Tor, iptables, sudo

### Web Crawler (Hakrawler)
- Fast link discovery
- Subdomain enumeration
- Configurable depth
- Requires: Go compiler

### Dark Web OSINT (TorBot)
- Scan .onion sites safely
- Extract information
- Link analysis
- Requires: Python 3.9+, Tor

### Network Pentesting (NetExec)
- Service enumeration
- Credential testing
- Active Directory attacks
- Protocols: SMB, RDP, SSH, LDAP, MSSQL

### Network Forensics (BruteShark)
- PCAP file analysis
- Credential extraction
- Hash cracking (Hashcat)
- Network mapping
- File carving

### System Information (PC-Info)
- Hardware inventory
- Software details
- Windows: Full PowerShell scan
- Linux: Python-based info

### Disk Benchmark
- Sequential R/W tests
- Random 4K tests
- Customizable size
- Real-time metrics

### Network Visualizer
- Interactive graphs
- Matplotlib powered
- Export PNG/PDF/SVG
- Crawler/TorBot integration

## 📚 Documentation

- **README_USB.txt** - USB portable guide
- **PORTABLE_PYTHON_GUIDE.md** - Embedded Python setup
- **FEATURES.md** - Detailed feature list
- **CHANGELOG.md** - Version history
- **LICENSE** - Legal information

## ⚙️ Configuration

### Settings Tab
- **Appearance**: Dark/Light/System theme
- **Auto-start**: Start Tor on launch
- **Notifications**: Enable/disable alerts

### Environment Variables
- `NETSAFE_USB_MODE=1` - Portable USB mode
- `PYTHONPATH` - Module search path

## 🔐 Security & Privacy

### Best Practices
✅ Use on authorized systems only
✅ Keep tools updated
✅ Use strong credentials
✅ Enable logging for audits
✅ Regular security reviews

### Privacy Features
- Tor network anonymization
- No telemetry or tracking
- Local data storage only
- Portable operation available
- Minimal system footprint

### Legal Compliance
⚠️ **Only use for:**
- Authorized security testing
- Personal privacy protection
- Educational purposes
- Research activities

❌ **Never use for:**
- Unauthorized access
- Illegal activities
- Data theft
- Network attacks

## 🤝 Contributing

Contributions welcome! Please:
1. Fork the repository
2. Create feature branch
3. Commit changes
4. Push to branch
5. Open Pull Request

## 📄 License

Main application: **MIT License**

Integrated tools: Various licenses (MIT, GPL-3.0, BSD-2, BSD-3)

See [LICENSE](LICENSE) file for complete details.

## 🙏 Credits

### Tool Developers
- **Nipe**: @htrgouvea (MIT)
- **Kalitorify**: @brainfucksec (GPL-3.0)
- **Hakrawler**: @hakluke (GPL-3.0)
- **TorBot**: @DedSecInside (GPL-3.0)
- **NetExec**: @Pennyw0rth (BSD-2)
- **BruteShark**: @odedshimon (GPL-3.0)
- **PC-information**: @nkhitrov (MIT)
- **CrossPlatformDiskTest**: @maxim-saplin (MIT)

### Frameworks
- **CustomTkinter**: @TomSchimansky
- **NetworkX**: NetworkX Team
- **Matplotlib**: Matplotlib Team
- **Tor Project**: The Tor Project

## 📞 Support

- **Documentation**: This README and included guides
- **Logs**: `logs/netsafe.log`
- **Issues**: GitHub Issues
- **Community**: Discord/Slack (coming soon)

## 🗺️ Roadmap

### Planned Features
- [ ] DNS leak protection
- [ ] Kill switch functionality
- [ ] Browser fingerprint protection
- [ ] Real-time PCAP sniffing
- [ ] AI-powered threat detection

## ⚡ Quick Commands

```bash
# Standard run
python main.py

# USB pre-install
python usb_preinstall.py

# Translate UI (developers)
python translate_gui.py

# Add tooltips (developers)
python add_tooltips.py

# Check errors
cat logs/netsafe.log
```

---

**🛡️ Stay Safe. Stay Anonymous. Stay Secure.**

*All-in-One Net Safe v3.0 - The Complete Security Toolkit*

*Last Updated: December 17, 2025*

