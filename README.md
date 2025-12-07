# 🛡️ Cenegi Security Scripts

A growing collection of penetration-testing, forensics, and security-automation scripts developed by **Cenegi**.  
These tools help streamline reconnaissance, scanning, analysis, and reporting tasks used in cybersecurity assessments, research, and lab environments.

> ⚠️ **Legal / Ethics**  
> These scripts are for **authorized testing only**.  
> Always obtain written permission before running any scans or analysis on systems or files you do not own.  
> Recon scripts include a **permission acknowledgment check** to prevent accidental misuse.

---

## 🔧 Features

- Easy-to-use command-line tools  
- Bash and Python versions for flexibility  
- Many tools support **proxychains** mode  
- **Colorized output** for readability (blue-themed for Cenegi branding)  
- Automated result directories with **timestamped logs**  
- Scripts include safe placeholder sections where appropriate  
- Forensics tools generate structured analysis reports  
- Designed as part of learning and building toward a larger Cenegi security platform  

More tools will be added over time as the project expands.

---

## 📜 Included Scripts

---

## 🔍 Penetration Testing Tools

### **1. `pentest-automation.sh` — Bash Recon Script**

Automates common early-stage penetration testing steps.

**Features:**
- Target-based recon with optional `--proxy` mode  
- Host discovery  
- Full TCP and UDP port scanning  
- Service enumeration  
- Banner grabbing  
- Optional integrations:
  - **Nikto** (web vulnerability scan)  
  - **sslscan** (TLS configuration review)  
  - **eyewitness** (web UI screenshots)

**Output:**  
Saves all scan data into a timestamped results folder.

---

### **2. `pentest_automation.py` — Python Recon Script**

A Python-based version mirroring the Bash workflow.

**Features:**
- TCP / UDP scanning, service detection, and banner grabbing  
- Proxy or normal mode  
- Auto-generated result directories  
- One-time permission acknowledgment (`.permission_ack`)  
- **Safe placeholders** for commands that must be intentionally filled in  
- Skips optional tools if not installed

---

## 🧪 File Forensics Tools

### **3. `forensic_file_scan.sh` — Bash File Analysis Script**

A lightweight forensic analyzer for single files.

**Modules included:**
- Metadata extraction  
- File type identification  
- MD5 / SHA1 / SHA256 hashing  
- Strings extraction  
- Suspicious keyword detection  
- Hex dump (first 256 bytes)  
- Entropy calculation  
- Final summary with module status flags  
- Generates a timestamped `.txt` report

Designed to be portable and dependency-minimal.

---

### **4. `forensic_file_scan.py` — Python File Analysis Script**

A more advanced Python version of the file analysis tool.

**Features:**
- Structured module-based design  
- Metadata, hashes, file type (`python-magic`), strings, hex dump  
- Entropy scoring  
- Suspicious string detection  
- Categorized module result flags  
- Final summary indicating whether the file shows potential malicious traits  
- Automatically generates detailed analysis reports

Cross-platform (Windows / Linux / macOS).

---

## 📁 Output Structure

### **Penetration Testing Scripts**

Each recon scan creates a directory:

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
 ├─ eyewitness_output/        # if installed
 └─ summary.txt
```
---

### **Forensics Tools Output**

Each file analysis creates a report:

`file_analysis_<filename>_<timestamp>.txt`

**Contents of the report include:**

- **Metadata** (size, timestamps, permissions)  
- **Hashes** (MD5, SHA1, SHA256)  
- **Strings & Suspicious Indicators**  
- **Hex Dump** (first 256 bytes)  
- **Entropy Score**  
- **Module-by-module status**  
  - e.g., COMPLETED, NONE FOUND, SUSPICIOUS FOUND  
- **Final Risk Summary**  
  - Indicates whether the file shows potentially malicious behavior  

---

## 🚀 Future Additions

This repository is part of a larger learning and development project.  
Planned enhancements include:

- Directory-wide forensics automation  
- YARA rule scanning  
- Malware signature correlation  
- PDF/Office macro extraction  
- PE/ELF deep analysis tools  
- Recon automation enhancements  
- Web enumeration modules  
- Windows-focused security utilities
