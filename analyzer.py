import re
import sys
from collections import Counter

LOG_FILE = "sample_auth.log"
THRESHOLD = int(sys.argv[1]) if len(sys.argv) > 1 else 3

ip_pattern = re.compile(r"(\d{1,3}\.){3}\d{1,3}")
failed_attempts = Counter()

with open(LOG_FILE, "r", encoding="utf-8", errors="ignore") as file:
    for line in file:
        if "failed password" in line.lower():
            match = ip_pattern.search(line)
            if match:
                ip = match.group()
                failed_attempts[ip] += 1

print(f"Suspicious IPs:" (threshold: {THRESHOLD}):") 
for ip, count in failed_attempts.items():
    if count >= THRESHOLD:
        print(f"{ip} -> {count} failed attempts")
