# Day 3-4: Log Summary Script using Python
# -----------------------------------------
# Demonstrates file creation, reading, and filtering (like grep/head/tail in Linux)

import os

print("🔍 Log Summary Script Running...")
print("Current Directory:", os.getcwd())

# Create 'logs' folder if it doesn't exist
log_dir = "logs"
os.makedirs(log_dir, exist_ok=True)
print("Folder Created:", os.path.join(os.getcwd(),"log_dir"))

# Define log file path
log_file = os.path.join(log_dir, "app.log")
print("log_file path:", os.path.join(log_dir, "app.log"))

from datetime import datetime
# Create a sample log file

with open(log_file, "w") as f:
    f.write(f"{datetime.now()} - error: network down\n")
    f.write(f"{datetime.now()} - info: service started\n")
    f.write(f"{datetime.now()} - warning: high memory usage\n")
    f.write(f"{datetime.now()} - error: timeout\n")

# Read the log file
with open(log_file, "r") as f:
    lines = f.readlines()

print(f"\nTotal lines: {len(lines)}")

# Filter for 'error' (like grep)
errors = [line.strip() for line in lines if "error" in line.lower()]

print("\nError lines:")
for e in errors:
    print("  ", e)

# Optional: Display first and last 2 lines (like head/tail)
print("\nFirst 2 lines (head):")
print("".join(lines[:2]))

print("Last 2 lines (tail):")
print("".join(lines[-2:]))


from collections import Counter

# Extract the first word of each line before the colon (:)
levels = [line.split(":")[0].strip().lower() for line in lines]

# Count how many times each appears
counts = Counter(levels)

print("\nLog level summary:")
for level, count in counts.items():
    print(f"  {level.capitalize()}: {count}")


from datetime import datetime

#creating a error_log file
error_log_path = os.path.join(log_dir, "error.log")
with open(error_log_path, "w") as ef:
    for e in errors:
        ef.write(e + "\n")

print(f"\nSaved {len(errors)} error lines to {error_log_path}")
