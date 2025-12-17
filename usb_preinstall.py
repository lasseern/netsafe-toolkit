#!/usr/bin/env python3
"""
Pre-Install Script for USB Version
Downloads and sets up all security tools in advance
"""

import os
import sys
import subprocess
import urllib.request
import platform
from pathlib import Path

class USBPreInstaller:
    """Pre-install all tools for USB version"""
    
    def __init__(self, base_dir=None):
        if base_dir is None:
            base_dir = os.path.dirname(os.path.abspath(__file__))
        
        self.base_dir = base_dir
        self.tools_dir = os.path.join(base_dir, "tools")
        
    def create_directories(self):
        """Create necessary directories"""
        print("Creating directory structure...")
        os.makedirs(self.tools_dir, exist_ok=True)
        os.makedirs(os.path.join(self.base_dir, "logs"), exist_ok=True)
        os.makedirs(os.path.join(self.base_dir, "data"), exist_ok=True)
        print("✓ Directories created")
    
    def check_git(self):
        """Check if git is installed"""
        try:
            subprocess.run(["git", "--version"], capture_output=True, check=True)
            return True
        except:
            print("⚠️  WARNING: Git not found. Some tools may not install.")
            return False
    
    def clone_repo(self, name, url):
        """Clone a git repository"""
        target_dir = os.path.join(self.tools_dir, name)
        
        if os.path.exists(target_dir):
            print(f"✓ {name} already exists")
            return True
        
        print(f"Cloning {name}...")
        try:
            subprocess.run(
                ["git", "clone", "--depth=1", url, target_dir],
                check=True,
                capture_output=True
            )
            print(f"✓ {name} cloned successfully")
            return True
        except subprocess.CalledProcessError as e:
            print(f"✗ Failed to clone {name}: {e}")
            return False
    
    def download_file(self, url, target_path):
        """Download a file"""
        try:
            print(f"Downloading {os.path.basename(target_path)}...")
            urllib.request.urlretrieve(url, target_path)
            print(f"✓ Downloaded successfully")
            return True
        except Exception as e:
            print(f"✗ Download failed: {e}")
            return False
    
    def install_nipe(self):
        """Install Nipe"""
        print("\n[1/10] Installing Nipe (Tor Routing)...")
        success = self.clone_repo("nipe", "https://github.com/htrgouvea/nipe")
        
        if success:
            nipe_dir = os.path.join(self.tools_dir, "nipe")
            print("  Note: Run 'sudo cpan install' in nipe directory on first use")
        
        return success
    
    def install_kalitorify(self):
        """Install Kalitorify"""
        print("\n[2/10] Installing Kalitorify (Transparent Proxy)...")
        success = self.clone_repo("kalitorify", "https://github.com/brainfucksec/kalitorify")
        
        if success:
            kalitorify_script = os.path.join(self.tools_dir, "kalitorify", "kalitorify.sh")
            if os.path.exists(kalitorify_script):
                os.chmod(kalitorify_script, 0o755)
                print("  Note: Kalitorify requires sudo and iptables on Linux")
        
        return success
    
    def install_hakrawler(self):
        """Install Hakrawler"""
        print("\n[3/10] Installing Hakrawler (Web Crawler)...")
        success = self.clone_repo("hakrawler", "https://github.com/hakluke/hakrawler")
        
        if success:
            print("  Note: Requires Go to build. Run 'go build' in hakrawler directory")
        
        return success
    
    def install_torbot(self):
        """Install TorBot"""
        print("\n[4/10] Installing TorBot (Dark Web OSINT)...")
        success = self.clone_repo("TorBot", "https://github.com/DedSecInside/TorBot")
        
        if success:
            print("  Note: Requires Python 3.9+. Install via GUI for virtualenv setup")
        
        return success
    
    def install_netexec(self):
        """Install NetExec info"""
        print("\n[5/10] NetExec (Network Pentesting)...")
        print("  Note: NetExec is installed via pipx. Run installation via GUI")
        print("  ✓ Marked for GUI installation")
        return True
    
    def install_pc_information(self):
        """Install PC-information"""
        print("\n[6/10] Installing PC-information (System Info)...")
        success = self.clone_repo("PC-information", "https://github.com/nkhitrov/PC-information")
        
        if success:
            print("  Note: Windows PowerShell script. Cross-platform mode uses Python")
        
        return success
    
    def install_disk_test(self):
        """Install Disk Test"""
        print("\n[7/10] Installing Disk Benchmark...")
        
        # Create Python-based benchmark
        disk_test_dir = os.path.join(self.tools_dir, "DiskTest")
        os.makedirs(disk_test_dir, exist_ok=True)
        
        print("  ✓ Python-based benchmark will be auto-created by application")
        return True
    
    def install_bruteshark(self):
        """Install BruteShark"""
        print("\n[8/10] Installing BruteShark (Network Forensics)...")
        
        is_windows = platform.system() == "Windows"
        bruteshark_dir = os.path.join(self.tools_dir, "BruteShark")
        os.makedirs(bruteshark_dir, exist_ok=True)
        
        if is_windows:
            url = "https://github.com/odedshimon/BruteShark/releases/latest/download/BruteSharkCli.exe"
            target = os.path.join(bruteshark_dir, "BruteSharkCli.exe")
            success = self.download_file(url, target)
        else:
            url = "https://github.com/odedshimon/BruteShark/releases/latest/download/BruteSharkCli"
            target = os.path.join(bruteshark_dir, "BruteSharkCli")
            success = self.download_file(url, target)
            if success and os.path.exists(target):
                os.chmod(target, 0o755)
        
        if success:
            print("  Note: Requires Npcap (Windows) or libpcap (Linux)")
        
        return success
    
    def install_networkx(self):
        """Install NetworkX"""
        print("\n[9/10] NetworkX (Visualization)...")
        print("  Note: Installed via pip in requirements.txt")
        print("  ✓ Marked for pip installation")
        return True
    
    def create_data_files(self):
        """Create additional data files"""
        print("\n[10/10] Creating additional files...")
        
        # Create README for tools directory
        readme_path = os.path.join(self.tools_dir, "README.txt")
        with open(readme_path, 'w') as f:
            f.write("""
All-in-One Net Safe - Tools Directory
=====================================

This directory contains all pre-installed security tools.

Installed Tools:
- nipe/                 : Tor routing engine (Perl)
- kalitorify/           : Transparent proxy (Bash)
- hakrawler/            : Web crawler (Go)
- TorBot/               : Dark web OSINT (Python)
- PC-information/       : System info (PowerShell)
- DiskTest/             : Disk benchmark (Python)
- BruteShark/           : Network forensics (C#/.NET)

Additional Tools (GUI Install):
- NetExec              : Installed via pipx
- NetworkX             : Installed via pip

All tools are ready to use from the GUI.
Some tools may require additional setup on first use.

For support, see main README.md
""")
        
        print("✓ Additional files created")
        return True
    
    def run_full_install(self):
        """Run complete pre-installation"""
        print("="*60)
        print("  All-in-One Net Safe - USB Pre-Installer")
        print("="*60)
        print()
        print(f"Installation directory: {self.base_dir}")
        print(f"Tools directory: {self.tools_dir}")
        print()
        
        # Check requirements
        git_available = self.check_git()
        if not git_available:
            print()
            response = input("Git is not available. Continue anyway? (y/N): ")
            if response.lower() != 'y':
                print("Installation cancelled.")
                return False
        
        print()
        print("Starting installation...")
        print()
        
        # Create directories
        self.create_directories()
        
        # Install each tool
        results = {
            "Nipe": self.install_nipe(),
            "Kalitorify": self.install_kalitorify(),
            "Hakrawler": self.install_hakrawler(),
            "TorBot": self.install_torbot(),
            "NetExec": self.install_netexec(),
            "PC-information": self.install_pc_information(),
            "DiskTest": self.install_disk_test(),
            "BruteShark": self.install_bruteshark(),
            "NetworkX": self.install_networkx(),
            "Data Files": self.create_data_files(),
        }
        
        # Summary
        print()
        print("="*60)
        print("  Installation Summary")
        print("="*60)
        print()
        
        for tool, success in results.items():
            status = "✓ SUCCESS" if success else "✗ FAILED"
            print(f"{tool:20} {status}")
        
        successful = sum(results.values())
        total = len(results)
        
        print()
        print(f"Completed: {successful}/{total} tools")
        print()
        
        if successful == total:
            print("✓ All tools installed successfully!")
            print()
            print("Next steps:")
            print("1. Copy this entire folder to your USB stick")
            print("2. Run START_USB_WINDOWS.bat (Windows) or START_USB_LINUX.sh (Linux)")
            print("3. Enjoy portable security tools!")
        else:
            print("⚠️  Some tools failed to install.")
            print("   The application will still work, but you may need to")
            print("   install missing tools via the GUI when needed.")
        
        print()
        print("="*60)
        
        return successful == total

if __name__ == "__main__":
    print()
    installer = USBPreInstaller()
    
    try:
        success = installer.run_full_install()
        sys.exit(0 if success else 1)
    except KeyboardInterrupt:
        print()
        print()
        print("Installation cancelled by user.")
        sys.exit(1)
    except Exception as e:
        print()
        print(f"FATAL ERROR: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
