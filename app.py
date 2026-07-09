#!/usr/bin/env python3

import platform
import socket
from datetime import datetime

OUTPUT_FILE = "/tmp/system_info.txt"

def generate_system_info():
    return f"""
========================================
System Information Report
========================================

Hostname : {socket.gethostname()}
OS       : {platform.system()}
Release  : {platform.release()}
Version  : {platform.version()}
Timestamp: {datetime.now()}

========================================
Python application executed successfully
========================================
"""

if __name__ == "__main__":

    report = generate_system_info()

    with open(OUTPUT_FILE, "w") as f:
        f.write(report)

    print(f"Report written to {OUTPUT_FILE}")
