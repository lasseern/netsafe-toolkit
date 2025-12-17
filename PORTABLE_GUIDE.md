# 💾 Portable USB Setup Guide

## Oversigt

All-in-One Net Safe kan køres direkte fra et USB-stick uden installation på værts-maskinen. Dette gør det perfekt til sikkerhedsarbejde på forskellige maskiner.

## 📋 Hvad Du Skal Bruge

- USB-stick (minimum 4GB anbefales)
- Windows eller Linux maskine med Python 3.8+
- Internet forbindelse (første gang for dependencies)

## 🔧 Setup Trin

### 1. Forbered USB-Stikket

```bash
# Kopier hele projektet til USB
cp -r "all in one net safe" /media/usb/
```

### 2. Windows Portable Setup

1. Åbn File Explorer
2. Naviger til USB-stikket
3. Find `start_windows.bat`
4. Højreklik → "Run as Administrator" (hvis påkrævet)
5. Vent mens dependencies installeres
6. Programmet starter automatisk

### 3. Linux Portable Setup

```bash
# Naviger til USB
cd /media/usb/all\ in\ one\ net\ safe/

# Gør launcher kørbar
chmod +x start_linux.sh

# Start program
./start_linux.sh
```

## 📁 Portable Directory Structure

```
USB:/all in one net safe/
├── start_windows.bat       # Windows launcher
├── start_linux.sh          # Linux launcher
├── portable_launcher.py    # Python launcher
├── main.py                 # Main application
├── requirements.txt        # Dependencies
├── modules/                # Application modules
├── tools/                  # Downloaded tools (Nipe, etc.)
├── logs/                   # Application logs
├── data/                   # User data
└── config/                 # Configuration files
```

## 🎯 Hvad Sker Der Ved Første Kørsel?

1. **Tjek Python**: Verificerer Python 3.8+ er tilgængelig
2. **Setup Miljø**: Opretter portable directories på USB
3. **Installer Dependencies**: Downloader nødvendige Python packages
4. **Start Application**: Launcher hovedprogrammet

## ⚙️ Portable Features

### Automatisk Environment Setup
- Alle paths er relative til USB-stikket
- Værktøjer downloades til USB:/tools/
- Logs gemmes på USB:/logs/
- Data og konfiguration på USB'en

### Cross-Platform Compatibility
- Windows: .bat launcher med PowerShell fallback
- Linux: Bash script med dependency checking
- Samme codebase, forskellige launchers

## 🔒 Sikkerhedsovervejelser

### ✅ Fordele
- Ingen spor på værts-maskinen
- Nem at transportere
- Fungerer på air-gapped systemer (efter første setup)
- Værktøjer og data følger med

### ⚠️ Ulemper
- Python skal være installeret på værts-maskinen
- Administrator-rettigheder nødvendige for nogle værktøjer
- USB hastighed kan påvirke performance
- Første kørsel kræver internet for dependencies

## 💡 Tips & Tricks

### Pre-Install Dependencies
For at undgå internet-krav:
```bash
# På en maskine med internet:
pip download -r requirements.txt -d usb_packages/

# På target maskine:
pip install --no-index --find-links=usb_packages -r requirements.txt
```

### Hurtigere USB Performance
- Brug USB 3.0+ stik
- Formatter som exFAT (Windows + Linux kompatibel)
- Defragmenter USB periodisk

### Backup Important Data
```bash
# Backup logs og data før du flytter USB
cp -r logs/ backup_logs/
cp -r data/ backup_data/
```

## 🐛 Fejlfinding

### "Python ikke fundet"
**Problem**: Python er ikke installeret på værts-maskinen
**Løsning**: Installer Python 3.8+ eller brug en maskine hvor det er installeret

### "Permission Denied"
**Problem**: Manglende rettigheder til at køre værktøjer
**Løsning**: Kør launcher som administrator

### "Module Not Found"
**Problem**: Dependencies ikke installeret korrekt
**Løsning**: Slet venv/ folder og kør launcher igen

### USB Ikke Genkendt
**Problem**: Filsystem ikke kompatibelt
**Løsning**: Formatter USB som exFAT eller FAT32

## 📊 Performance Optimering

### Reducer Disk I/O
- Brug SSD USB-stick når muligt
- Cache værktøj-downloads lokalt
- Kom preinstallerede tools på USB'en

### Memory Optimization
- Luk andre programmer under scanning
- Begræns crawl dybde for store sites
- Clear visualization data efter brug

## 🔄 Opdatering

For at opdatere portable installation:

```bash
# På USB-stikket
git pull origin main

# Eller download ny version og overskriv filer
# Bevar logs/ og data/ directories
```

## 📞 Support

Ved problemer:
1. Tjek [README.md](README.md) for generel dokumentation
2. Se application logs i `logs/netsafe.log`
3. Rapporter issues på GitHub

---

**Note**: Portable mode er designet til fleksibilitet. For permanent installation på en enkelt maskine, brug standard installation metoden.
