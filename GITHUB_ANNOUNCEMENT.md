# 🎉 All-in-One Net Safe v2.0 - Major Update Release

## 🚀 What's New

I'm excited to announce **version 2.0** of All-in-One Net Safe - a massive update that expands the toolkit from 36 to **55 comprehensive security, privacy, and network tools**!

This release represents a complete overhaul with 19 brand new features, all with fully implemented GUIs and robust backend controllers.

---

## ✨ New Features (19 Total)

### 🔒 Security Enhancements (6 Features)

#### **WiFi Password Recovery**
- Extract all saved WiFi passwords from Windows
- Export passwords to file
- View network authentication and encryption details

#### **Password Vault**
- Encrypted password manager with master password
- Fernet symmetric encryption
- Add, edit, delete password entries
- Secure local storage

#### **2FA/TOTP Authenticator**
- Generate 2FA codes compatible with Google Authenticator
- Auto-refresh codes with countdown timer
- QR code provisioning support
- Secure secret storage

#### **Steganography**
- Hide secret messages inside images using LSB method
- Extract hidden messages from images
- Supports PNG, JPG, BMP formats
- Capacity calculator

#### **Encrypted Containers**
- Create password-protected encrypted file containers
- PBKDF2HMAC key derivation (100,000 iterations)
- Mount/unmount containers
- Add and extract files securely

#### **Keylogger Detector**
- Scan running processes for suspicious behavior
- Detect keyboard hooks and DLL injection
- Suspicion level scoring (0-10)
- Real-time process analysis

---

### 🌐 Network Tools (5 Features)

#### **VPN Manager**
- Manage Windows VPN connections via rasdial
- Connect/disconnect VPNs
- View connection status
- List all configured VPNs

#### **Speed Test**
- Internet speed testing (download/upload/ping)
- Server selection and distance calculation
- Real-time progress updates
- Export results

#### **DNS Changer**
- Change DNS servers with one click
- Presets: Google, Cloudflare, OpenDNS, Quad9, AdGuard
- Custom DNS configuration
- Network interface selection
- DHCP auto-configuration

#### **Packet Sniffer**
- Real-time packet capture (requires admin)
- Protocol analysis (TCP, UDP, ICMP, etc.)
- Statistics by protocol
- Export to CSV
- Source/destination IP and port display

#### **Wake-on-LAN**
- Send magic packets to wake network devices
- Save device list for quick access
- MAC address validation
- Custom broadcast address support

---

### 🛡️ Security Monitoring (5 Features)

#### **Anti-Ransomware Protection**
- Honeypot file monitoring system
- Real-time file change detection
- Instant alerts for suspicious activity
- Configurable monitoring directories

#### **File Integrity Monitor**
- SHA-256 baseline creation for critical files
- Continuous integrity monitoring
- Detect unauthorized file modifications
- Change type identification (modified/deleted/added)

#### **USB Monitor**
- Track USB device connections and disconnections
- Event logging with timestamps
- Block USB autorun for security
- Device information capture

#### **Network Traffic Analyzer**
- Real-time bandwidth monitoring
- Active connection tracking
- Upload/download rate display
- Process identification
- Packet statistics

#### **Log Analyzer**
- Windows Event Log analysis
- Threat pattern detection
- Filter by log type (System, Application, Security)
- Severity classification
- Recent critical events display

---

### 🧰 System Utilities (3 Features)

#### **System Cleaner**
- Scan temp files, Windows temp, browser cache
- Display cleanable space by category
- Individual or bulk cleanup
- Empty recycle bin
- Detailed statistics (file count, MB freed)

#### **Duplicate Finder**
- Hash-based duplicate file detection (MD5)
- Recursive directory scanning
- Size grouping for efficiency
- Wasted space calculation
- Duplicate group visualization

#### **QR Code Generator**
- Generate QR codes for URLs, text, WiFi credentials
- Customizable size and error correction
- WiFi QR codes with SSID and password
- Save to PNG format
- High-quality output

---

## 🔧 Technical Improvements

### Backend Enhancements
- **19 new controller classes** (~3,100 lines of code)
- Comprehensive error handling in all modules
- Threaded operations for non-blocking UI
- Windows API integration (WMI, Registry, PowerShell)
- Security best practices (encryption, hashing, secure deletion)

### GUI Updates
- **1,800+ lines** of new GUI code
- Modern CustomTkinter dark theme throughout
- Real-time feedback and progress indicators
- Intuitive dialogs and wizards
- Export/save functionality for all features
- Consistent user experience across all tools

### Dependencies Added
```python
cryptography>=41.0.0     # Encryption
pyotp>=2.9.0            # 2FA/TOTP
qrcode>=7.4.2           # QR generation
pyzbar>=0.1.9           # QR scanning
speedtest-cli>=2.1.3    # Speed testing
pywin32>=306            # Windows integration
```

---

## 📊 Statistics

| Metric | Value |
|--------|-------|
| **Total Features** | 55 (36 existing + 19 new) |
| **Lines of Code Added** | ~4,900 |
| **New Controllers** | 19 |
| **GUI Implementations** | 19 complete interfaces |
| **New Dependencies** | 6 packages |
| **Windows Integration** | netsh, wmic, rasdial, PowerShell |

---

## 🎯 Feature Highlights by Category

### All 55 Features Organized

#### 🔒 Security & Privacy (14)
Password Generator, Password Vault, 2FA/TOTP, Hash Calculator, Steganography, Encrypted Containers, File Shredder, Metadata Cleaner, Keylogger Detector, Anti-Ransomware, SSL Checker, WiFi Password Recovery, Browser Fingerprint Protection, WebRTC Leak Protection

#### 🌐 Network Tools (13)
Port Scanner, Network Sniffer, Packet Sniffer, Network Traffic Analyzer, Device Scanner, DNS Leak Test, VPN Manager, DNS Changer, Speed Test, Wake-on-LAN, Proxy Checker, WHOIS Lookup, DoH Configuration

#### 🕵️ Anonymity & Tor (4)
Tor Network, Kalitorify, Dark Web Crawler, Kill Switch

#### 🛡️ System Monitoring (9)
File Integrity Monitor, USB Monitor, Log Analyzer, Firewall Manager, Traffic Monitor, Network Visualizer, PC Information, Disk Health Test, BruteShark

#### 🧰 System Utilities (10)
System Cleaner, Duplicate Finder, MAC Changer, QR Code Generator, Email Header Analyzer, NetExec, Startup Manager, Service Manager, Update Manager, Settings

---

## 🚀 Getting Started

### Installation

1. **Clone the repository:**
```bash
git clone https://github.com/lasseern/all-in-one-net-safe.git
cd all-in-one-net-safe
```

2. **Install dependencies:**
```bash
pip install -r requirements.txt
```

3. **Run the application:**
```bash
python main.py
```

### Requirements
- Windows 10/11
- Python 3.12+
- Administrator rights (for some features)

---

## ⚠️ Important Notes

### Features Requiring Admin Rights
- Packet Sniffer (raw socket access)
- Firewall Manager (Windows Firewall rules)
- Service Manager (Windows service control)
- USB Monitor (WMI device monitoring)
- DNS Changer (network interface configuration)

### Security Recommendations
1. **Password Vault:** Use a strong master password (minimum 8 characters)
2. **Encrypted Containers:** Store in secure locations only
3. **2FA/TOTP:** Backup secret keys securely
4. **Anti-Ransomware:** Enable before any suspicious activity
5. **File Integrity:** Create baselines for critical directories

---

## 🐛 Bug Fixes

- Fixed PBKDF2 import in encrypted container controller
- Resolved threading issues during GUI initialization
- Improved error handling across all network features
- Enhanced stability for long-running monitoring tasks

---

## 🔜 Future Roadmap

- macOS and Linux support
- Cloud backup integration for Password Vault
- Advanced network monitoring with ML-based anomaly detection
- Mobile companion app for 2FA/TOTP
- Plugin system for community extensions
- Automated threat response system

---

## 🤝 Contributing

Contributions are welcome! Please feel free to submit pull requests, report bugs, or suggest new features.

### Ways to Contribute
- 🐛 Report bugs and issues
- 💡 Suggest new features
- 📝 Improve documentation
- 🔧 Submit pull requests
- ⭐ Star the repository

---

## 📄 License

MIT License - See [LICENSE](LICENSE) for details

Copyright (c) 2025 lasseern

---

## 🙏 Acknowledgments

Special thanks to all the open-source projects that make this toolkit possible:
- CustomTkinter for the modern GUI framework
- cryptography for encryption implementations
- pyotp for 2FA support
- All third-party tools integrated (Tor, Nipe, Kalitorify, etc.)

---

## 📞 Contact & Support

- **GitHub:** [@lasseern](https://github.com/lasseern)
- **Issues:** [Report a bug](https://github.com/lasseern/all-in-one-net-safe/issues)
- **Discussions:** [Join the conversation](https://github.com/lasseern/all-in-one-net-safe/discussions)

---

**⭐ If you find this project useful, please consider giving it a star!**

---

*Created with ❤️ by lasseern*

**Version 2.0 - December 2025**
