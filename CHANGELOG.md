# 📝 Changelog - All-in-One Net Safe

## Version 3.0 - December 2025

### 🎉 Major Update: 3 New Security Tools Added

#### ✨ New Features

##### 💻 PC Information Tool
- **Integration**: PC-information by nkhitrov
- **License**: MIT
- **Capabilities**:
  - Full Windows system scan via PowerShell
  - Cross-platform basic info mode (Python/psutil)
  - Hardware inventory (CPU, RAM, BIOS, Motherboard)
  - Software and OS information
  - Network adapter details
  - Disk information

##### 💾 Disk Benchmark Tool
- **Integration**: CrossPlatformDiskTest by maxim-saplin
- **License**: MIT
- **Capabilities**:
  - Sequential read/write testing
  - Random 4K block testing
  - Customizable test sizes (10-10000 MB)
  - Cross-platform support (Windows, Linux, macOS)
  - Real-time performance metrics
  - MB/s speed measurements

##### 🦈 Network Forensics Tool (BruteShark)
- **Integration**: BruteShark by odedshimon
- **License**: GPL-3.0
- **Capabilities**:
  - PCAP/PCAPNG file analysis
  - Credential extraction (HTTP, FTP, Telnet, IMAP, SMTP)
  - Hash extraction (NTLM, Kerberos, CRAM-MD5, HTTP-Digest)
  - Network topology mapping
  - DNS query extraction
  - File carving from TCP/UDP sessions
  - VoIP call extraction (SIP, RTP)
  - Hashcat integration for hash cracking

#### 🎨 GUI Enhancements
- Added 3 new tabs to main interface:
  - 💻 PC Info tab with full/basic scan modes
  - 💾 Disk Test tab with benchmark controls
  - 🦈 BruteShark tab with PCAP analysis
- Total tabs increased from 8 to 11
- Improved tab organization and navigation
- Enhanced status indicators

#### 📚 Documentation Updates
- Updated README.md with 10 integrated tools
- Enhanced FEATURES.md with detailed tool descriptions
- Updated LICENSE with proper attributions
- Added all new tool licenses and copyrights

#### 🔧 Technical Improvements
- New controller modules:
  - `pc_info_controller.py`
  - `disk_test_controller.py`
  - `bruteshark_controller.py`
- Enhanced error handling
- Improved threading for background tasks
- Better cross-platform compatibility

#### 📦 Dependencies
- All Python dependencies maintained in requirements.txt
- psutil for system information (already included)
- Cross-platform PowerShell/Python fallback support

---

## Version 2.0 - November 2025

### 🚀 Major Features

#### ⚡ NetExec Integration
- Network penetration testing
- Protocol support: SMB, RDP, WinRM, SSH, LDAP, MSSQL
- Active Directory enumeration
- Credential testing

#### 📊 Network Visualization
- NetworkX integration
- Interactive graph visualization
- Export to PNG/PDF/SVG
- Crawler and TorBot result visualization

#### 💾 Portable USB Support
- Windows launcher (start_windows.bat)
- Linux launcher (start_linux.sh)
- Portable environment setup
- Self-contained installation

---

## Version 1.0 - Initial Release

### 🎯 Core Tools

#### 🔐 Nipe (Tor Routing)
- Tor network integration
- System-wide traffic routing
- IPv4/IPv6 support

#### 🛡️ Kalitorify (Transparent Proxy)
- Kali Linux specialized
- Iptables-based routing
- Complete system anonymity

#### 🕷️ Hakrawler (Web Crawler)
- Fast web crawling
- Subdomain discovery
- Configurable depth
- Link extraction

#### 🌑 TorBot (Dark Web OSINT)
- .onion site scanning
- Dark web intelligence
- Link analysis

### 🎨 GUI Features
- Modern CustomTkinter interface
- Dark/Light/System theme support
- Danish language interface
- Real-time status updates
- Threaded operations
- Comprehensive logging

---

## 📊 Statistics

- **Total Integrated Tools**: 10
- **GUI Tabs**: 11
- **Controllers**: 10
- **Supported Platforms**: Windows, Linux, macOS (partial)
- **License Types**: MIT, GPL-3.0, BSD-2, BSD-3
- **Lines of Code**: ~3000+

---

## 🔮 Roadmap for Version 4.0

### Planned Features
- [ ] VPN integration
- [ ] DNS leak protection
- [ ] Kill switch functionality
- [ ] Browser fingerprint protection
- [ ] Real-time PCAP sniffing
- [ ] AI-powered threat detection
- [ ] Automated reporting system
- [ ] Plugin architecture
- [ ] Multi-language support (English, German)
- [ ] Cloud data synchronization

### Under Consideration
- Mobile companion app
- Web interface
- REST API
- Docker containerization
- Kubernetes deployment
- CI/CD integration

---

## 🙏 Contributors

Special thanks to all the original tool developers:
- @htrgouvea (Nipe)
- @brainfucksec (Kalitorify)
- @hakluke (Hakrawler)
- @DedSecInside (TorBot)
- @Pennyw0rth (NetExec)
- @nkhitrov (PC-information)
- @maxim-saplin (CrossPlatformDiskTest)
- @odedshimon (BruteShark)

And the framework maintainers:
- @TomSchimansky (CustomTkinter)
- NetworkX Team
- Matplotlib Team
- The Tor Project

---

**Date**: December 17, 2025
**Maintainer**: All-in-One Net Safe Team
**License**: MIT (Main App) + Various (Integrated Tools)

🛡️ For a safer, more private internet experience.
