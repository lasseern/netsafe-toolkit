# All-in-One Net Safe - Complete Feature List

**Created by:** lasseern  
**Version:** 2.0  
**Total Features:** 55  
**Platform:** Windows  
**GUI:** CustomTkinter (Modern Dark Theme)

---

## 🔒 Security & Privacy Tools (14 Features)

### Password & Authentication
- **Password Generator** - Generate secure passwords with customizable complexity
- **Password Vault** - Encrypted password manager with Fernet encryption
- **2FA/TOTP Authenticator** - Generate 2FA codes with auto-refresh (compatible with Google Authenticator)
- **Hash Calculator** - Calculate MD5, SHA-1, SHA-256, SHA-512 hashes

### Data Protection
- **Steganography** - Hide/extract secret messages in images using LSB method
- **Encrypted Containers** - Create secure file containers with PBKDF2HMAC encryption
- **File Shredder** - Securely delete files with multi-pass overwriting
- **Metadata Cleaner** - Remove metadata from images and documents

### Security Analysis
- **Keylogger Detector** - Scan processes for keyloggers, detect keyboard hooks
- **Anti-Ransomware** - Honeypot-based ransomware detection with real-time alerts
- **SSL/TLS Checker** - Verify SSL certificates and security
- **WiFi Password Recovery** - Extract and export saved WiFi passwords

### Privacy Protection
- **Browser Fingerprint Protection** - Reduce browser fingerprinting
- **WebRTC Leak Protection** - Prevent WebRTC IP leaks

---

## 🌐 Network Tools (13 Features)

### Network Analysis
- **Port Scanner** - Scan for open ports on target hosts
- **Network Sniffer** - Capture and analyze network packets
- **Packet Sniffer** - Real-time packet capture with protocol analysis (requires admin)
- **Network Traffic Analyzer** - Monitor bandwidth usage and active connections
- **Device Scanner** - Discover devices on local network
- **DNS Leak Test** - Check for DNS leaks

### Network Management
- **VPN Manager** - Manage Windows VPN connections
- **DNS Changer** - Change DNS servers with presets (Google, Cloudflare, OpenDNS, Quad9, AdGuard)
- **Speed Test** - Test internet connection speed (download/upload/ping)
- **Wake-on-LAN** - Send magic packets to wake network devices
- **Proxy Checker** - Test and validate proxy servers
- **WHOIS Lookup** - Domain and IP information lookup
- **DoH Configuration** - Configure DNS-over-HTTPS

---

## 🕵️ Anonymity & Tor (4 Features)

### Tor Network
- **Tor Network** - Route traffic through Tor network
- **Kalitorify** - Transparent proxy through Tor
- **Dark Web Crawler** - Search and navigate dark web (onion sites)
- **Kill Switch** - Emergency network kill switch

---

## 🛡️ System Monitoring & Protection (9 Features)

### Security Monitoring
- **File Integrity Monitor** - SHA-256 baseline monitoring for file changes
- **USB Monitor** - Track USB device connections, block autorun
- **Log Analyzer** - Analyze Windows Event Logs for threats
- **Firewall Manager** - Manage Windows Firewall rules

### System Analysis
- **Traffic Monitor** - Monitor and visualize network traffic
- **Network Visualizer** - Visual representation of network connections
- **PC Information** - Comprehensive system information
- **Disk Health Test** - Check disk health and S.M.A.R.T. status
- **BruteShark** - Network forensics analysis

---

## 🧰 System Utilities (10 Features)

### File Management
- **System Cleaner** - Clean temp files, cache, and recycle bin
- **Duplicate Finder** - Find duplicate files using hash comparison
- **MAC Changer** - Spoof MAC address

### Information Tools
- **QR Code Generator** - Generate QR codes (URL, WiFi, Text)
- **Email Header Analyzer** - Analyze email headers for security info
- **NetExec** - Network execution and administration tools

### System Management
- **Startup Manager** - Manage Windows startup programs
- **Service Manager** - Control Windows services
- **Update Manager** - Check for system and application updates
- **Settings** - Application configuration and preferences

---

## 📊 Feature Categories Summary

| Category | Features | Key Technologies |
|----------|----------|------------------|
| **Security & Privacy** | 14 | Fernet, PBKDF2, SHA-256, LSB Steganography |
| **Network Tools** | 13 | Raw Sockets, netsh, rasdial, speedtest-cli |
| **Anonymity & Tor** | 4 | Tor, SOCKS5 Proxy |
| **System Monitoring** | 9 | WMI, Event Logs, SHA-256, psutil |
| **System Utilities** | 10 | Registry, WMI, PowerShell |
| **Configuration** | 5 | Settings, About, Themes |

**Total:** 55 Features

---

## 🔧 Technical Stack

### Core Technologies
- **Language:** Python 3.12+
- **GUI Framework:** CustomTkinter (Modern Dark Theme)
- **Encryption:** cryptography (Fernet, PBKDF2HMAC)
- **Network:** socket, psutil, scapy, requests
- **System:** pywin32, WMI, PowerShell integration

### Key Dependencies
```
customtkinter>=5.2.0
psutil>=5.9.0
cryptography>=41.0.0
pyotp>=2.9.0
qrcode>=7.4.2
pyzbar>=0.1.9
speedtest-cli>=2.1.3
pywin32>=306
requests>=2.31.0
Pillow>=10.0.0
scapy>=2.5.0
```

---

## 🎯 Use Cases

### For Security Professionals
- Network analysis and packet capture
- Security auditing and vulnerability scanning
- Log analysis and threat detection
- File integrity monitoring

### For Privacy-Conscious Users
- Anonymous browsing through Tor
- Encrypted file storage
- Secure password management
- Data steganography

### For System Administrators
- Network device management
- Service and startup control
- System monitoring and cleanup
- DNS and VPN configuration

### For General Users
- Speed testing and network diagnostics
- QR code generation
- Duplicate file cleanup
- WiFi password recovery

---

## ⚠️ Requirements

- **OS:** Windows 10/11
- **Python:** 3.12 or higher
- **Privileges:** Some features require administrator rights
  - Packet Sniffer
  - Firewall Manager
  - Service Manager
  - DNS Changer
  - USB Monitor

---

## 📝 License

MIT License - Copyright (c) 2025 lasseern

See LICENSE file for full details and third-party attributions.

---

**Created with ❤️ by lasseern**
