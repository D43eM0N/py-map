#  PyMap: Modular Network Discovery & Security Auditor

![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

**PyMap** is an interactive, CLI-based networking utility designed for rapid LAN reconnaissance and security auditing. It provides a modular environment similar to professional penetration testing frameworks, allowing users to switch between host discovery and port auditing seamlessly.

---

## Features

* **Interactive Shell:** A custom-built command-line interface with state management (`use`, `back`, `exit`).
* ** PingSweep Module:** * Active host discovery across local subnets.
    * Network interface metadata extraction (IP, Subnet Mask, Gateway).
    * Hostname resolution for identified devices.
* ** PortScanner Module:**
    * TCP service identification on specific targets.
    * Common port mapping (SMB, RDP, RPC, etc.).
    * Optimized socket timeout handling for efficient scanning.

---

## Visual Showcase

```text
┌────────────────────────────────────────┐

     | < > |    PYMAP NETWORK    | < > |
    
      _____       __  __                
     |  __ \     |  \/  |               
     | |__) |   _| \  / | __ _ _ __     
     |  ___/ | | | |\/| |/ _` | '_ \    
     | |   | |_| | |  | | (_| | |_) |   
     |_|    \__, |_|  |_|\__,_| .__/    
             __/ |            | |       
            |___/             |_|       

└────────────────────────────────────────┘

  [1] [PingSweep Module] Scan LAN/Gather Information about Net
  [2] [Port Scan]

──────────────────────────────────────────

Welcome to PyMap!
Type help or -h to list commands. Type exit to quit.

PyMap >
```
## Installation & Usage
Prerequisites
Python 3.8+

No external libraries required (Uses standard asyncio, socket, and subprocess).

Setup
Bash
# Clone the repository
git clone https://github.com/D43eM0N/py-map.git

# Navigate to directory
cd PyMap

# Launch PyMap
python pymap.py
Quick Commands
Host Scan: use 1 -> pingsweep -d [IP] -n [Interface] -s

Port Scan: use 2 -> portscanner -d [Target_IP] -s

 Technical Implementation
This tool was developed to explore low-level networking concepts:

Asynchronous I/O: Utilizes asyncio to perform non-blocking port scans, significantly increasing speed compared to sequential scanning.

Socket Programming: Direct implementation of the socket library for TCP handshaking and service detection.

Modular Design: A clean separation between the CLI controller and the networking logic, allowing for easy expansion.

# License

License
Copyright © 2025 D43eM0N

This project is licensed under the MIT License. See the LICENSE file for details.

## Contributing & Feedback

This is my first project, and I am committed to improving its efficiency and security. If you have any suggestions, performance improvements, or find any bugs, please feel free to open an Issue or submit a Pull Request. All constructive feedback is welcome!
