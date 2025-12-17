#!/usr/bin/env python3
"""
All-in-One Net Safe - Sikkerhedsprogram til anonym internetbrowsing
"""

import customtkinter as ctk
from modules.nipe_controller import NipeController
from modules.gui import NetSafeGUI
import logging
from pathlib import Path

# Opsæt logging
LOG_DIR = Path(__file__).parent / "logs"
LOG_DIR.mkdir(exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(LOG_DIR / "netsafe.log"),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)


def main():
    """Start hovedapplikationen"""
    logger.info("Starting All-in-One Net Safe...")
    
    # Sæt udseende
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")
    
    # Start GUI
    app = NetSafeGUI()
    app.mainloop()


if __name__ == "__main__":
    main()
