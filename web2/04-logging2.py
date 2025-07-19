# py 04-logging2.py

import logging

log_path="system.log"

try:
    with open (log_path, "r") as f:
        print(f"Reading file:{log_path}")
        for line in f:
            if "ERROR" in line:
                print("WARNING:",line.strip())
except FileNotFoundError:
    print(f"Log file not found:{log_path}")