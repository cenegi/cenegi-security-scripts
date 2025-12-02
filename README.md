# Cenegi Security Scripts

A collection of penetration‑testing and security‑automation scripts developed by Cenegi.  
These tools are designed to speed up reconnaissance, scanning, and workflow tasks commonly used in security assessments.

---

## 🔧 Features

- Easy-to-use command-line interface  
- Optional `--proxy` flag for routing tools through **proxychains**  
- Colorized output for readability (using blue‑themed variants)  
- Modular design so additional tools can be added over time  

---

## 📜 Included Scripts

### **Pentest Automation Script**
A bash script that:
- Asks if you want to use `proxychains` (or accepts `--proxy` flag)
- Runs recon/scanning commands automatically
- Outputs color-coded status messages
- Useful for repeatable assessment workflows

File: `pentest-automation.sh`

---

## 🚀 Usage

Run normally:
```bash
./pentest-automation.sh

Run with proxychains:

./pentest-automation.sh --proxy


Make executable:

chmod +x pentest-automation.sh


