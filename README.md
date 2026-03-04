# 🛰️ PyMap: Modular Network Discovery & Security Auditor

![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

**PyMap** is an interactive, CLI-based networking utility designed for rapid LAN reconnaissance and security auditing. It provides a modular environment similar to professional penetration testing frameworks, allowing users to switch between host discovery and port auditing seamlessly.

---

## 🛠️ Features

* **Interactive Shell:** A custom-built command-line interface with state management (`use`, `back`, `exit`).
* **📡 PingSweep Module:** * Active host discovery across local subnets.
    * Network interface metadata extraction (IP, Subnet Mask, Gateway).
    * Hostname resolution for identified devices.
* **🔍 PortScanner Module:**
    * TCP service identification on specific targets.
    * Common port mapping (SMB, RDP, RPC, etc.).
    * Optimized socket timeout handling for efficient scanning.

---

## 🖥️ Visual Showcase

```text
┌────────────────────────────────────────┐
| < > |    PYMAP NETWORK    | < > |
|  _____    ___  __                |
| |  __ \  |  \/  |                |
| | |__) | _| \  / | __ _ _ __     |
| |  ___/ | | | |\/| |/ _` | '_ \    |
| | |   | |_| | |  | | (_| | |_) |   |
| |_|    \__, |_|  |_|\__,_| .__/    |
|         __/ |            | |       |
|        |___/             |_|       |
└────────────────────────────────────────┘
## 🚀 Installation & Usage

### Prerequisites
* Python 3.8+
* Scapy or relevant networking libraries

### Setup
```bash
# Clone the repository
git clone https://github.com/D43eM0N/py-map.git

# Navigate to directory
cd py-map

# Install dependencies
pip install -r requirements.txt

# Launch PyMap
python pymap.py
