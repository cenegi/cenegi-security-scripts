# 🛡️ Cenegi Security Scripts

A small collection of penetration-testing and security-automation scripts developed by **Cenegi**.  
These tools streamline reconnaissance, scanning, and documentation tasks commonly used in security assessments and lab work.

> ⚠️ **Legal / Ethics**  
> These scripts are for **authorized testing and lab environments only**.  
> Always obtain written permission from the system owner before running any security tests.

---

## 🔧 Features

- **Easy-to-use command-line interface**
- Optional `--proxy` flag for routing tools through **proxychains**
- **Colorized output** for readability (blue-themed highlight styles)
- Modular layout so additional scripts can be added over time
- Designed to be readable and easily customized for different engagements

---

## 📜 Included Scripts

### 1. **Pentest Automation Script** (`pentest-automation.sh`)

Bash-based automation helper that:

- Prompts whether to use `proxychains` or accepts the `--proxy` flag  
- Runs a sequence of recon / scanning commands (e.g., host discovery, port scans, service enumeration)  
- Uses color-coded status messages for clarity  
- Saves output in a structured way so you can quickly review findings later  
- Acts as a repeatable baseline workflow for assessments and lab practice

---

## ⚙️ Requirements

- Linux system (Kali or similar recommended)
- Common assessment tools installed (e.g., `nmap`, `proxychains`, etc.)
- Executable permissions on the script:

```bash
chmod +x pentest-automation.sh
---

