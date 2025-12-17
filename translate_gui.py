#!/usr/bin/env python3
"""
Translation script to convert gui.py from Danish to English
"""

import re

# Translation dictionary - Danish to English
translations = {
    # Docstrings
    "Opsæt brugergrænsefladen": "Set up the user interface",
    "Opret header med logo og titel": "Create header with logo and title",
    "Opret hovedindholdsområdet": "Create main content area",
    "Opsæt Tor Network tab": "Set up Tor Network tab",
    "Opsæt Kalitorify tab": "Set up Kalitorify tab",
    "Opsæt Web Crawler tab (Hakrawler)": "Set up Web Crawler tab (Hakrawler)",
    "Opsæt Dark Web OSINT tab (TorBot)": "Set up Dark Web OSINT tab (TorBot)",
    "Opsæt PC Information tab": "Set up PC Information tab",
    "Opsæt Disk Test tab": "Set up Disk Test tab",
    "Opsæt BruteShark tab": "Set up BruteShark tab",
    "Opsæt indstillinger tab": "Set up settings tab",
    "Opsæt om-tab": "Set up about tab",
    "Opret footer med statusbar": "Create footer with statusbar",
    "Installer Nipe i baggrunden": "Install Nipe in the background",
    "Start eller stop Tor routing": "Start or stop Tor routing",
    "Genstart Tor (få ny circuit)": "Restart Tor (get new circuit)",
    "Opdater status display": "Update status display",
    "Opdater UI med status (køres på main thread)": "Update UI with status (runs on main thread)",
    "Opdater footer besked": "Update footer message",
    "Skift appearance mode": "Change appearance mode",
    "Installer Kalitorify": "Install Kalitorify",
    "Start/stop Kalitorify": "Start/stop Kalitorify",
    "Genstart Kalitorify": "Restart Kalitorify",
    "Installer Hakrawler": "Install Hakrawler",
    "Start web crawl": "Start web crawl",
    "Installer TorBot": "Install TorBot",
    "Start TorBot scan": "Start TorBot scan",
    "Installer NetExec": "Install NetExec",
    "Kør NetExec scan": "Run NetExec scan",
    "Visualiser crawler resultater": "Visualize crawler results",
    "Visualiser TorBot resultater": "Visualize TorBot results",
    "Vis visualisering i GUI": "Show visualization in GUI",
    "Gem visualisering til fil": "Save visualization to file",
    "Clear visualisering": "Clear visualization",
    "Opsæt NetExec tab": "Set up NetExec tab",
    "Opsæt Network Visualizer tab": "Set up Network Visualizer tab",
    
    # UI Labels
    "Sikker og anonym internetbrowsing": "Secure and anonymous internet browsing",
    "Status:": "Status:",
    "Inaktiv": "Inactive",
    "Aktiv ✓": "Active ✓",
    "IP Adresse:": "IP Address:",
    "Ikke tilgængelig": "Not available",
    "Land:": "Country:",
    "Dybde:": "Depth:",
    "Inkluder subdomæner": "Include subdomains",
    "Scan Dybde:": "Scan Depth:",
    "Brug SOCKS5 proxy (Tor)": "Use SOCKS5 proxy (Tor)",
    "Udseende:": "Appearance:",
    "Start Tor automatisk ved programstart": "Start Tor automatically on program start",
    "Vis notifikationer": "Show notifications",
    "Klar til brug": "Ready to use",
    
    # Buttons
    "📥 Installer Nipe": "📥 Install Nipe",
    "▶️ Start Tor": "▶️ Start Tor",
    "⏹️ Stop Tor": "⏹️ Stop Tor",
    "🔄 Ny Circuit": "🔄 New Circuit",
    "📥 Installer Kalitorify": "📥 Install Kalitorify",
    "▶️ Start Proxy": "▶️ Start Proxy",
    "⏹️ Stop Proxy": "⏹️ Stop Proxy",
    "🔄 Genstart Tor": "🔄 Restart Tor",
    "📥 Installer Hakrawler": "📥 Install Hakrawler",
    "🚀 Start Crawl": "🚀 Start Crawl",
    "📥 Installer TorBot": "📥 Install TorBot",
    "🔍 Scan Site": "🔍 Scan Site",
    "📥 Installer": "📥 Install",
    "🔍 Full System Scan (Windows)": "🔍 Full System Scan (Windows)",
    "💡 Basic Info (Cross-platform)": "💡 Basic Info (Cross-platform)",
    "🚀 Run Benchmark": "🚀 Run Benchmark",
    "ℹ️ Disk Info": "ℹ️ Disk Info",
    "📁 Browse": "📁 Browse",
    "🔍 Analyze PCAP": "🔍 Analyze PCAP",
    "✔️ Check Prerequisites": "✔️ Check Prerequisites",
    "📈 Vis Crawler Data": "📈 Show Crawler Data",
    "🌐 Vis TorBot Data": "🌐 Show TorBot Data",
    "💾 Gem Graf": "💾 Save Graph",
    "🗑️ Clear": "🗑️ Clear",
    
    # Placeholders
    "C:\\\\Temp eller /tmp (lad tom for default)": "C:\\\\Temp or /tmp (leave empty for default)",
    "192.168.1.0/24 eller domain.com": "192.168.1.0/24 or domain.com",
    "Vælg PCAP fil...": "Select PCAP file...",
    
    # Messages  
    "Fejl": "Error",
    "Succes": "Success",
    "Advarsel": "Warning",
    "Installation fejlede": "Installation failed",
    "Installerer...": "Installing...",
    "Starter...": "Starting...",
    "Stopper...": "Stopping...",
    "Genstarter...": "Restarting...",
    "Crawler...": "Crawling...",
    "Scanner...": "Scanning...",
    "Klar": "Ready",
    "Installerer Nipe...": "Installing Nipe...",
    "Installerer Kalitorify...": "Installing Kalitorify...",
    "Installerer Hakrawler...": "Installing Hakrawler...",
    "Kloner Kalitorify...": "Cloning Kalitorify...",
    "Kloner TorBot...": "Cloning TorBot...",
    "Starter Tor routing...": "Starting Tor routing...",
    "Stopper Tor routing...": "Stopping Tor routing...",
    "Genstarter Tor circuit...": "Restarting Tor circuit...",
    "Ny Tor circuit aktiveret": "New Tor circuit activated",
    "Genstart fejlede": "Restart failed",
    "Tor routing aktiveret": "Tor routing enabled",
    "Tor routing deaktiveret": "Tor routing disabled",
    "Kunne ikke starte Tor": "Could not start Tor",
    "Kunne ikke stoppe Tor": "Could not stop Tor",
    "Crawl fuldført": "Crawl completed",
    "Scan fuldført": "Scan completed",
    "Visualisering opdateret": "Visualization updated",
    "Visualisering cleared": "Visualization cleared",
    "Disk info hentet": "Disk info retrieved",
    "NetExec scan fuldført": "NetExec scan completed",
    "Henter system information...": "Getting system information...",
    "Henter basic system info...": "Getting basic system info...",
    "Kører disk benchmark... Dette kan tage et stykke tid...": "Running disk benchmark... This may take a while...",
    "Henter disk info...": "Getting disk info...",
    "Downloader BruteShark CLI...": "Downloading BruteShark CLI...",
    "Checker afhængigheder...": "Checking dependencies...",
    "Scanning system... Vent venligst...": "Scanning system... Please wait...",
    "Scanning system...": "Scanning system...",
    
    # Longer messages
    "Indtast venligst en URL": "Please enter a URL",
    "Indtast venligst en .onion URL": "Please enter a .onion URL",
    "Indtast venligst et target": "Please enter a target",
    "Ingen crawler data tilgængelig. Kør en crawl først.": "No crawler data available. Run a crawl first.",
    "Ingen TorBot data tilgængelig. Kør en scan først.": "No TorBot data available. Run a scan first.",
    "Kunne ikke finde URLs i crawler resultater": "Could not find URLs in crawler results",
    "Kunne ikke finde .onion URLs i TorBot resultater": "Could not find .onion URLs in TorBot results",
    "Vælg en PCAP fil først": "Select a PCAP file first",
    "Vælg mindst ét modul": "Select at least one module",
    "Test størrelse skal være mellem 10-10000 MB": "Test size must be between 10-10000 MB",
    "Ugyldig størrelse": "Invalid size",
    "Ingen data at gemme": "No data to save",
    "Ingen data at visualisere endnu.\\n\\nBrug Crawler eller TorBot først.": "No data to visualize yet.\\n\\nUse Crawler or TorBot first.",
    "Vælg PCAP fil": "Select PCAP file",
    "Vælg output mappe (eller annuller for ingen export)": "Select output folder (or cancel for no export)",
    "Manglende afhængigheder:": "Missing dependencies:",
    "Check fejlede": "Check failed",
    
    # Info text blocks
    "Tor Network router al din internettrafik gennem Tor-netværket": "Tor Network routes all your internet traffic through the Tor network",
    "for at beskytte din anonymitet og privatliv online.": "to protect your anonymity and privacy online.",
    "OBS: Dette kræver administrator-rettigheder og er kun": "NOTE: This requires administrator privileges and is only",
    "tilgængeligt på Linux/Unix systemer.": "available on Linux/Unix systems.",
    "Windows-brugere skal bruge WSL (Windows Subsystem for Linux).": "Windows users must use WSL (Windows Subsystem for Linux).",
    
    "Transparent proxy gennem Tor for Kali Linux": "Transparent proxy through Tor for Kali Linux",
    "Kalitorify er designet til Kali Linux og opretter en transparent": "Kalitorify is designed for Kali Linux and creates a transparent",
    "proxy gennem Tor-netværket ved hjælp af iptables.": "proxy through the Tor network using iptables.",
    "OBS: Kun til Kali Linux eller Debian-baserede systemer.": "NOTE: Only for Kali Linux or Debian-based systems.",
    "Kræver administrator-rettigheder.": "Requires administrator privileges.",
}

def translate_file(input_file, output_file=None):
    """Translate Danish text to English in file"""
    if output_file is None:
        output_file = input_file
    
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Apply translations
    for danish, english in translations.items():
        content = content.replace(danish, english)
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"Translation complete: {input_file} -> {output_file}")

if __name__ == "__main__":
    translate_file("e:\\all in one net safe\\modules\\gui.py")
    print("GUI translated to English!")
