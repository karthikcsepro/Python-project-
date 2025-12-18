#!/bin/python3
import sys
import socket
from datetime import datetime as dt

if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1])
else:
    print("Invalid number of arguments")
    print("Usage: python3 scanner.py <ip>")
    sys.exit()

print("-" * 50)
print(f"Scanning Target: {target}")
print(f"Time Started: {dt.now()}")
print("-" * 50)

try:
    for port in range(1, 1025):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.05)

        if s.connect_ex((target, port)) == 0:
            print(f"Port {port} is OPEN")

        s.close()

except KeyboardInterrupt:
    print("\nScan stopped by user")
    sys.exit()

except socket.error:
    print("Unable to connect to target")
    sys.exit()
