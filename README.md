# 🛡️ Cenegi Security Scripts

A collection of penetration‑testing and security‑automation scripts developed by **Cenegi**.  
These tools streamline reconnaissance, scanning, and workflow tasks commonly used in security assessments.

---

## 🔧 Features

- **Easy-to-use command-line interface**
- Optional `--proxy` flag for routing tools through **proxychains**
- **Colorized output** for readability (blue‑themed highlight styles)
- Modular design — more scripts can be added over time

---

## 📜 Included Scripts

### **Pentest Automation Script** (`pentest-automation.sh`)
A Bash-based automation tool that:

- Asks whether you want to use `proxychains` or accepts the `--proxy` flag  
- Runs recon and scanning commands automatically  
- Uses color-coded status messages for clarity  
- Serves as a fast, repeatable assessment workflow  

---

## 🚀 Usage

### Run normally:
```bash
./pentest-automation.sh
