# 🛡️ Cenegi Security Scripts

A small collection of penetration-testing and security-automation scripts developed by **Cenegi**.  
These tools streamline reconnaissance, scanning, and documentation tasks commonly used in security assessments and lab environments.

> ⚠️ **Legal / Ethics**  
> These scripts are for **authorized testing only**.  
> Always obtain written permission from the system owner before running any security tests.  
> The Python version includes a **permission acknowledgment prompt** to confirm authorization before any commands are executed.

---

## 🔧 Features

- **Easy-to-use command-line interface**
- Supports both **normal** and **proxychains** modes  
- **Colorized output** (blue-themed for consistency with Cenegi branding)
- Saves scan artifacts, enumerated data, and reports into a **timestamped results directory**
- Bash and Python versions maintain the same workflow
- Python version includes **safe placeholders** that must be manually filled in with the real scanning commands before use

---

## 📜 Included Scripts

### 1. `pentest-automation.sh` — Bash Recon Script

The Bash script:

- Accepts a target IP and an optional `--proxy` flag  
- Runs automated recon steps:
  - Host discovery  
  - TCP/UDP scanning  
  - Service enumeration  
  - Banner grabbing  
- Optionally integrates:
  - **Nikto** (web scanning)  
  - **sslscan** (TLS/SSL checks)  
  - **eyewitness** (web UI screenshots)
- Saves all results into a unique directory named after the target and timestamp

---

### 2. `pentest_automation.py` — Python Recon Script

Python-based version that mirrors the Bash workflow:

- Includes all major modules: TCP scan, UDP scan, service detection, banner grabbing, optional web checks  
- Supports both normal and proxy modes  
- Automatically creates output directories and log files  
- Adds a **one-time permission acknowledgment** (`.permission_ack`)  
- Includes **placeholder commands** (commented or printed) where real recon commands should be added  
  - Prevents accidental scanning without intentional configuration  
- Safe by default, customizable as needed

---

## ⚙️ Requirements

### Required Tools
- `nmap`  
- `nc` (netcat)

### Optional Tools
Used only if installed:

- `nikto` — Web vulnerability scanning  
- `sslscan` — SSL/TLS configuration review  
- `eyewitness` — Web UI screenshot capture  
- `proxychains` — Enables proxy mode for routing traffic

If optional tools are missing, scripts automatically skip those sections.

---

## 📁 Output Structure

Each scan creates a timestamped results directory:

```text
results_<target>_<timestamp>/
 ├─ ping_results.txt
 ├─ nmap_all_ports.txt
 ├─ nmap_udp_scan.txt
 ├─ nmap_detailed_scan.txt
 ├─ nmap_vuln_scan.txt
 ├─ banners.txt
 ├─ nikto_results.txt
 ├─ sslscan_results.txt
 ├─ eyewitness_output/        # if eyewitness is installed
 └─ summary.txt
