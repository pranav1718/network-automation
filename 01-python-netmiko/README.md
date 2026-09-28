# Section 01: Network Automation with Python & Netmiko

This section covers multi-vendor network device interaction using Python and Netmiko. It includes foundational SSH connections, push configurations, and structured output parsing using TextFSM and Cisco pyATS/Genie.

---

## 📁 Repository Structure

| File | Description |
| :--- | :--- |
| `Netmiko_Basics.py` | Establishes SSH connections, authenticates using privilege 15, and executes basic `show` commands. |
| `Config_Changes.py` | Pushes configuration command sets (`send_config_set`) to network devices. |
| `Text_FSM.py` | Parses unstructured CLI command outputs (`show interfaces`) into structured Python dictionaries using TextFSM. |
| `Genie.py` | Demonstrates structured data extraction using Cisco pyATS / Genie parsers (`use_genie=True`). |

---

## 🛠️ Prerequisites & Setup

### 1. Python Environment Dependencies
Install the required Python packages:

```bash
pip install netmiko ntc-templates rich

2. Note on Cisco pyATS / Genie (Windows vs Linux)
Note: pyATS and Genie require POSIX system calls (pty, termios) and cannot be run directly on native Windows.

To run Genie.py, execute the script inside WSL (Ubuntu on Windows) or a Linux container where pip install pyats genie is supported.

For native Windows execution, use use_textfsm=True with ntc-templates.

🚀 Usage
Running Scripts Locally
Execute any script via Python:

python Netmiko_Basics.py
python Config_Changes.py
python Text_FSM.py
Running Genie Parsers via WSL (Linux Subsystem)
Bash
cd /mnt/c/Users/User/network-automation/01-python-netmiko
python3 Genie.py
🔐 Credentials & Lab Topology
Device Type: cisco_ios

Target Host: Lab Gateway / Virtual Router (192.168.x.x)

Authentication: Local AAA / Privilege 15 user credentials


## Sequential vs Parallel Execution

### 1. Sequential Execution (`Loops.py`)
Iterates through network devices listed in `inventory.py` sequentially using a `for` loop. Connects to each router one-by-one to retrieve operational status (`show ip int brief`).

- **Pros:** Easy to debug, low CPU memory footprint.
- **Cons:** Slow when scaling across large inventories since latency accumulates per device.

### 2. Multi-Threaded Execution (`Threading.py`)
Utilizes Python's `concurrent.futures.ThreadPoolExecutor` (or `threading` module) to open SSH connections to all target devices concurrently.

- **Pros:** Significantly faster completion times across multi-device deployments.
- **Cons:** Requires thread synchronization and error handling for connection timeouts.



