import subprocess
import sys
import socket

# Function to ping a subdomain and get its IP address
def ping_and_get_ip(subdomain):
    try:
        # Resolve the IP address for the subdomain
        ip = socket.gethostbyname(subdomain)
        return subdomain, ip
    except socket.gaierror:
        return None

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python ping.py filename")
        exit(1)

    filename = sys.argv[1]

    try:
        with open(filename, 'r') as file:
            subdomains = file.read().splitlines()
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
        exit(1)

    results = []

    for subdomain in subdomains:
        result = ping_and_get_ip(subdomain)
        if result is not None:
            results.append(result)

    for subdomain, ip in results:
        print(f"{subdomain} {ip}")
