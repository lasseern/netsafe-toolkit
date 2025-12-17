#!/usr/bin/env python3
"""
Script to add tooltips to all buttons in gui.py
"""

import re

def add_tooltips_to_buttons():
    """Add tooltip calls after each button .grid() call"""
    
    with open("e:\\all in one net safe\\modules\\gui.py", 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    # Button to tooltip mapping
    button_tooltips = {
        "Install Nipe": 'ToolTip(self.install_btn, TOOLTIPS["tor_install"])',
        "Start Tor": 'ToolTip(self.toggle_btn, TOOLTIPS["tor_start"])',
        "New Circuit": 'ToolTip(self.restart_btn, TOOLTIPS["tor_circuit"])',
        "Install Kalitorify": 'ToolTip(self.kalitorify_install_btn, TOOLTIPS["kalitorify_install"])',
        "Start Proxy": 'ToolTip(self.kalitorify_toggle_btn, TOOLTIPS["kalitorify_start"])',
        "Restart Tor": 'ToolTip(self.kalitorify_restart_btn, TOOLTIPS["kalitorify_restart"])',
        "Install Hakrawler": 'ToolTip(self.crawler_install_btn, TOOLTIPS["crawler_install"])',
        "Start Crawl": 'ToolTip(self.crawler_start_btn, TOOLTIPS["crawler_start"])',
        "Install TorBot": 'ToolTip(self.torbot_install_btn, TOOLTIPS["darkweb_install"])',
        "Scan Site": 'ToolTip(self.torbot_scan_btn, TOOLTIPS["darkweb_scan"])',
        "Full System Scan": 'ToolTip(self.pcinfo_full_btn, TOOLTIPS["pcinfo_full"])',
        "Basic Info": 'ToolTip(self.pcinfo_basic_btn, TOOLTIPS["pcinfo_basic"])',
        "Run Benchmark": 'ToolTip(self.disktest_run_btn, TOOLTIPS["disktest_run"])',
        "Disk Info": 'ToolTip(self.disktest_info_btn, TOOLTIPS["disktest_info"])',
        "Analyze PCAP": 'ToolTip(self.bruteshark_analyze_btn, TOOLTIPS["bruteshark_analyze"])',
        "Check Prerequisites": 'ToolTip(self.bruteshark_check_btn, TOOLTIPS["bruteshark_check"])',
        "Show Crawler Data": 'ToolTip(viz_crawler_btn, TOOLTIPS["visualizer_crawler"])',
        "Show TorBot Data": 'ToolTip(viz_torbot_btn, TOOLTIPS["visualizer_torbot"])',
        "Save Graph": 'ToolTip(viz_save_btn, TOOLTIPS["visualizer_save"])',
    }
    
    new_lines = []
    i = 0
    while i < len(lines):
        line = lines[i]
        new_lines.append(line)
        
        # Check if this is a button grid line
        if '.grid(' in line and 'ctk.CTkButton' in ''.join(lines[max(0, i-10):i]):
            # Look for the button text in previous lines
            context = ''.join(lines[max(0, i-10):i+1])
            
            for button_text, tooltip_code in button_tooltips.items():
                if f'"{button_text}"' in context or f"'{button_text}'" in context:
                    # Check if tooltip not already added
                    if i+1 < len(lines) and 'ToolTip' not in lines[i+1]:
                        # Add tooltip on next line with proper indentation
                        indent = len(line) - len(line.lstrip())
                        new_lines.append(' ' * indent + tooltip_code + '\n')
                    break
        
        i += 1
    
    # Write back
    with open("e:\\all in one net safe\\modules\\gui.py", 'w', encoding='utf-8') as f:
        f.writelines(new_lines)
    
    print("Tooltips added to all buttons!")

if __name__ == "__main__":
    add_tooltips_to_buttons()
