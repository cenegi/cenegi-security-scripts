#!/usr/bin/env python3

import os
import sys
import hashlib
import magic
import math
from datetime import datetime

# ------------------------
# Entropy Calculation
# ------------------------
def calculate_entropy(file_path):
    with open(file_path, "rb") as f:
        data = f.read()
    if len(data) == 0:
        return 0.0

    byte_counts = [0] * 256
    for byte in data:
        byte_counts[byte] += 1

    entropy = 0
    for count in byte_counts:
        if count == 0:
            continue
        p = count / len(data)
        entropy -= p * math.log(p, 2)

    return entropy


# ------------------------
# Hashing Function
# ------------------------
def file_hash(path, algo="sha256"):
    h = hashlib.new(algo)
    with open(path, "rb") as f:
        while chunk := f.read(8192):
            h.update(chunk)
    return h.hexdigest()


# ------------------------
# Strings Extraction
# ------------------------
def extract_strings(path, min_length=4):
    good_chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789/\\:._-"
    results = []

    with open(path, "rb") as f:
        current = ""
        while byte := f.read(1):
            char = chr(byte[0])
            if char in good_chars:
                current += char
            else:
                if len(current) >= min_length:
                    results.append(current)
                current = ""
        if len(current) >= min_length:
            results.append(current)

    return results


# ------------------------
# Suspicious Pattern Detection
# ------------------------
SUSPICIOUS_PATTERNS = [
    "powershell",
    "cmd.exe",
    "wget",
    "curl",
    "shellcode",
    "base64",
    "eval(",
    "import os",
    "import subprocess",
]

def detect_suspicious(strings):
    suspicious = []
    for s in strings:
        for pat in SUSPICIOUS_PATTERNS:
            if pat.lower() in s.lower():
                suspicious.append(s)
    return suspicious


# ------------------------
# Hex dump (first 256 bytes)
# ------------------------
def hex_dump(path, size=256):
    with open(path, "rb") as f:
        chunk = f.read(size)
        return chunk.hex(" ", 1)


# ------------------------
# MAIN REPORT GENERATOR
# ------------------------
def generate_report(file_path):
    report_name = f"file_analysis_{os.path.basename(file_path)}_{int(datetime.now().timestamp())}.txt"
    m = {}

    # Module results flags
    module_results = {}

    # Metadata
    stat = os.stat(file_path)
    m["metadata"] = {
        "size": stat.st_size,
        "modified": datetime.fromtimestamp(stat.st_mtime),
        "created": datetime.fromtimestamp(stat.st_ctime),
        "permissions": oct(stat.st_mode)[-3:]
    }
    module_results["METADATA"] = "COMPLETED"

    # Hashes
    m["hashes"] = {
        "md5": file_hash(file_path, "md5"),
        "sha1": file_hash(file_path, "sha1"),
        "sha256": file_hash(file_path, "sha256")
    }
    module_results["HASHES"] = "COMPLETED"

    # File type
    try:
        m["file_type"] = magic.from_file(file_path)
        module_results["FILE TYPE"] = "COMPLETED"
    except Exception:
        m["file_type"] = "Unable to detect"
        module_results["FILE TYPE"] = "FAILED"

    # Strings
    strings = extract_strings(file_path)
    suspicious = detect_suspicious(strings)
    m["strings"] = strings[:50]
    m["suspicious"] = suspicious

    if suspicious:
        module_results["STRINGS"] = "SUSPICIOUS FOUND"
    else:
        module_results["STRINGS"] = "NONE FOUND"

    # Hex dump
    m["hex_dump"] = hex_dump(file_path)
    module_results["HEX DUMP"] = "COMPLETED"

    # Entropy
    entropy = calculate_entropy(file_path)
    m["entropy"] = entropy
    if entropy > 7.5:
        module_results["ENTROPY"] = "HIGH ENTROPY (Possible packed or encrypted)"
    else:
        module_results["ENTROPY"] = "NORMAL"

    # Suspicious summary flag
    if suspicious or entropy > 7.5:
        m["malicious_indicator"] = True
    else:
        m["malicious_indicator"] = False

    # ------------------------
    # WRITE REPORT
    # ------------------------

    with open(report_name, "w") as r:
        r.write("===== FILE ANALYSIS REPORT =====\n")
        r.write(f"File: {file_path}\n")
        r.write(f"Generated: {datetime.now()}\n\n")

        # Metadata
        r.write("[METADATA]\n")
        for k, v in m["metadata"].items():
            r.write(f"{k}: {v}\n")

        r.write("\n[HASHES]\n")
        for algo, val in m["hashes"].items():
            r.write(f"{algo}: {val}\n")

        r.write("\n[FILE TYPE]\n")
        r.write(f"{m['file_type']}\n")

        r.write("\n[STRINGS] (First 50)\n")
        for s in m["strings"]:
            r.write(f"{s}\n")

        r.write("\n[SUSPICIOUS STRINGS]\n")
        if m["suspicious"]:
            for s in m["suspicious"]:
                r.write(f"{s}\n")
        else:
            r.write("None found.\n")

        r.write("\n[HEX DUMP] (First 256 bytes)\n")
        r.write(m["hex_dump"] + "\n")

        r.write("\n[ENTROPY]\n")
        r.write(f"{entropy}\n")

        # SUMMARY
        r.write("\n===================================\n")
        r.write("              SUMMARY\n")
        r.write("===================================\n\n")
        for module, result in module_results.items():
            r.write(f"{module}: {result}\n")

        r.write("\nPotential Malicious Indicators: ")
        r.write("YES\n" if m["malicious_indicator"] else "NO\n")

        r.write("===================================\n")

    print(f"\nReport generated: {report_name}")


# ------------------------
# ENTRY POINT
# ------------------------
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python forensic_file_scan.py <file>")
        sys.exit(1)

    file_path = sys.argv[1]

    if not os.path.isfile(file_path):
        print("Error: File not found.")
        sys.exit(1)

    generate_report(file_path)
