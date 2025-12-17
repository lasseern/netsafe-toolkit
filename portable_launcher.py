"""
Portable Launcher - Gør programmet portable til USB sticks
"""

import sys
import os
from pathlib import Path
import platform
import subprocess


def setup_portable_environment():
    """Opsæt portable miljø"""
    # Få script directory
    if getattr(sys, 'frozen', False):
        # Running as compiled executable
        app_dir = Path(sys.executable).parent
    else:
        # Running as script
        app_dir = Path(__file__).parent.parent
    
    # Tilføj app dir til PATH
    os.environ['PYTHONPATH'] = str(app_dir)
    
    # Sæt portable directories
    portable_dirs = {
        'TOOLS_DIR': app_dir / 'tools',
        'LOGS_DIR': app_dir / 'logs',
        'DATA_DIR': app_dir / 'data',
        'CONFIG_DIR': app_dir / 'config'
    }
    
    # Opret directories hvis de ikke eksisterer
    for dir_path in portable_dirs.values():
        dir_path.mkdir(parents=True, exist_ok=True)
    
    # Sæt environment variables
    for key, value in portable_dirs.items():
        os.environ[key] = str(value)
    
    return app_dir, portable_dirs


def check_python_version():
    """Tjek Python version"""
    if sys.version_info < (3, 8):
        print("Error: Python 3.8+ er påkrævet")
        print(f"Din version: {sys.version}")
        return False
    return True


def install_dependencies(app_dir: Path):
    """Installer dependencies hvis de mangler"""
    requirements_file = app_dir / 'requirements.txt'
    
    if not requirements_file.exists():
        print("Warning: requirements.txt ikke fundet")
        return False
    
    try:
        print("Tjekker dependencies...")
        # Prøv at importere customtkinter
        import customtkinter
        print("✓ Dependencies allerede installeret")
        return True
    except ImportError:
        print("Installerer dependencies...")
        subprocess.run([
            sys.executable, '-m', 'pip', 'install', '-r', str(requirements_file)
        ])
        return True


def main():
    """Main launcher funktion"""
    print("=" * 60)
    print("  All-in-One Net Safe - Portable Launcher")
    print("=" * 60)
    
    # Tjek Python version
    if not check_python_version():
        input("\nTryk Enter for at afslutte...")
        return
    
    # Setup portable environment
    app_dir, portable_dirs = setup_portable_environment()
    print(f"\n✓ Portable miljø opsat: {app_dir}")
    
    # Installer dependencies hvis nødvendigt
    install_dependencies(app_dir)
    
    # Start main application
    print("\nStarter All-in-One Net Safe...\n")
    main_script = app_dir / 'main.py'
    
    if main_script.exists():
        # Importer og kør main
        sys.path.insert(0, str(app_dir))
        import main
        main.main()
    else:
        print(f"Error: Kunne ikke finde {main_script}")
        input("\nTryk Enter for at afslutte...")


if __name__ == "__main__":
    main()
