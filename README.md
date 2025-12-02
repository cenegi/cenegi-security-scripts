# 🛡️ Cenegi Security Scripts

A small collection of penetration-testing and security-automation scripts developed by **Cenegi**.  
These tools streamline reconnaissance, scanning, and documentation tasks commonly used in security assessments and lab work.

> ⚠️ **Legal / Ethics**  
> These scripts are for **authorized testing and lab environments only**.  
> Always obtain written permission from the system owner before running any security tests.

---

## 🔧 Features

- **Easy-to-use command-line interface**
- Supports both **normal** and **proxychains** modes
- **Colorized output** for readability (blue-themed highlight styles)
- Saves all artifacts (scans, banners, web results, screenshots, summary) into a **timestamped results folder**
- Designed to be readable and easily customized for different engagements

---

## 📜 Included Scripts

### 1. Pentest Automation Script – `pentest-automation.sh`

Bash-based automation helper that:

- Takes a target IP and an optional `--proxy` flag  
- Runs a sequence of recon / scanning commands (host discovery, port scans, service enumeration)  
- Collects banners from open ports  
- Optionally runs:
  - **Nikto** for web application checks  
  - **sslscan** for TLS/SSL checks  
  - **eyewitness** for web UI screenshots  
- Writes everything into a dedicated results directory for that run

---

## ⚙️ Requirements

**Required tools:**

- `nmap`
- `nc` (netcat)

If these are missing, the script will stop and tell you what to install.

**Optional tools (used if present):**

- `nikto` – web vulnerability scanning
- `sslscan` – SSL/TLS configuration checks
- `eyewitness` – web screenshot capture
- `proxychains` – for proxy mode

If optional tools are not installed, the script will simply skip those steps and print a notice.

---

## 📁 Output Structure

Each run creates a separate results folder:

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
 ├─ eyewitness_output/        # (if eyewitness is installed)
 └─ summary.txt
