#!/bin/bash

# Simple Forensic File Analysis Script
# Generates a detailed text report with summary + module result flags.

FILE="$1"
REPORT="file_analysis_$(basename "$FILE")_$(date +%s).txt"

if [[ -z "$FILE" || ! -f "$FILE" ]]; then
    echo "Usage: $0 <file>"
    exit 1
fi

# Initialize module result flags
META_RESULT="NOT RUN"
HASH_RESULT="NOT RUN"
TYPE_RESULT="NOT RUN"
STRING_RESULT="NOT RUN"
HEX_RESULT="NOT RUN"
ENTROPY_RESULT="NOT RUN"
SUSPICIOUS_RESULT="NOT RUN"

# Calculate entropy
calculate_entropy() {
    awk '{
        for (i = 1; i <= length($0); i++) {
            b[substr($0, i, 1)]++
            total++
        }
    }
    END {
        entropy = 0
        for (c in b) {
            p = b[c] / total
            entropy -= p * log(p) / log(2)
        }
        print entropy
    }' "$1"
}

# Run modules and log everything
echo "===== FILE ANALYSIS REPORT =====" > "$REPORT"
echo "File: $FILE" >> "$REPORT"
echo "Generated: $(date)" >> "$REPORT"

#############################################
# MODULE: Metadata
#############################################
echo -e "\n[METADATA MODULE]" >> "$REPORT"
stat "$FILE" >> "$REPORT"
META_RESULT="COMPLETED"

#############################################
# MODULE: Hashes
#############################################
echo -e "\n[HASH MODULE]" >> "$REPORT"
MD5=$(md5sum "$FILE" | awk '{print $1}')
SHA1=$(sha1sum "$FILE" | awk '{print $1}')
SHA256=$(sha256sum "$FILE" | awk '{print $1}')
echo "MD5: $MD5" >> "$REPORT"
echo "SHA1: $SHA1" >> "$REPORT"
echo "SHA256: $SHA256" >> "$REPORT"
HASH_RESULT="COMPLETED"

#############################################
# MODULE: File Type
#############################################
echo -e "\n[FILE TYPE MODULE]" >> "$REPORT"
file "$FILE" >> "$REPORT"
TYPE_RESULT="COMPLETED"

#############################################
# MODULE: Strings Extraction
#############################################
echo -e "\n[STRINGS MODULE]" >> "$REPORT"
strings "$FILE" | head -n 50 >> "$REPORT"

# Check suspicious keywords
SUSP=$(strings "$FILE" | grep -Ei "exec|powershell|cmd\.exe|wget|curl|shellcode|base64" | wc -l)

if [[ $SUSP -gt 0 ]]; then
    echo -e "\nSuspicious strings detected: $SUSP" >> "$REPORT"
    STRING_RESULT="SUSPICIOUS FOUND"
    SUSPICIOUS_RESULT="YES"
else
    echo -e "\nNo suspicious strings found." >> "$REPORT"
    STRING_RESULT="NONE FOUND"
fi

#############################################
# MODULE: Hex Dump
#############################################
echo -e "\n[HEX DUMP MODULE] (First 256 bytes)" >> "$REPORT"
xxd -l 256 "$FILE" >> "$REPORT"
HEX_RESULT="COMPLETED"

#############################################
# MODULE: Entropy
#############################################
echo -e "\n[ENTROPY MODULE]" >> "$REPORT"
ENTROPY=$(calculate_entropy "$FILE")
echo "Entropy: $ENTROPY" >> "$REPORT"

if (( $(echo "$ENTROPY > 7.5" | bc -l) )); then
    ENTROPY_RESULT="HIGH ENTROPY (Possible packed or encrypted)"
    SUSPICIOUS_RESULT="YES"
else
    ENTROPY_RESULT="NORMAL"
fi

#############################################
# SUMMARY SECTION
#############################################

echo -e "\n===================================" >> "$REPORT"
echo "              SUMMARY" >> "$REPORT"
echo "===================================" >> "$REPORT"
echo "File: $FILE" >> "$REPORT"
echo -e "\nModule Results:" >> "$REPORT"
echo "METADATA:   $META_RESULT" >> "$REPORT"
echo "HASHES:     $HASH_RESULT" >> "$REPORT"
echo "FILE TYPE:  $TYPE_RESULT" >> "$REPORT"
echo "STRINGS:    $STRING_RESULT" >> "$REPORT"
echo "HEX DUMP:   $HEX_RESULT" >> "$REPORT"
echo "ENTROPY:    $ENTROPY_RESULT" >> "$REPORT"

if [[ "$SUSPICIOUS_RESULT" == "YES" ]]; then
    echo -e "\nPotential Malicious Indicators: YES" >> "$REPORT"
else
    echo -e "\nPotential Malicious Indicators: NO" >> "$REPORT"
fi

echo "===================================" >> "$REPORT"

echo "Report generated: $REPORT"
