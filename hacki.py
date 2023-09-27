import subprocess
import socket
import sys

# Function to ping an IP address and return True if it's reachable, False otherwise
def is_ip_reachable(ip):
    try:
        result = subprocess.check_output(['ping', '-c', '1', ip])
        return "1 packets transmitted, 1 received" in result.decode()
    except subprocess.CalledProcessError:
        return False

# Function to read IP addresses from a given file
def read_ips_from_file(filename):
    with open(filename, 'r') as file:
        return [line.strip() for line in file]

# Function to perform HTTP requests with different IPs using curl
def curl_with_ips(ips, subdomains_file):
    for ip in ips:
        with open(subdomains_file, 'r') as sub_file:
            for subdomain in sub_file:
                subdomain = subdomain.strip()
                curl_command = f'curl {ip} -H "Host: {subdomain}"'
                print(f"Executing: {curl_command}")
                result = subprocess.run(curl_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                
                # Add a border around the response
                border = "=" * 100
                print(border)
                print(result.stdout.decode())
                print(border)
                print(result.stderr.decode())

# Main script
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python vhost.py subdomains_file")
        sys.exit(1)

    subdomains_file = sys.argv[1]

    # Check if subdomains are reachable and extract IPs
    ips = []
    subdomains = []
    with open(subdomains_file, 'r') as sub_file:
        for subdomain in sub_file:
            subdomain = subdomain.strip()
            subdomains.append(subdomain)
            try:
                ip = socket.gethostbyname(subdomain)
                ips.append(ip)
            except socket.gaierror:
                print(f"Unable to resolve IP for subdomain: {subdomain}")

    # Filter only reachable IPs
    reachable_ips = [ip for ip in ips if is_ip_reachable(ip)]

    if len(reachable_ips) == 0:
        print("No reachable IPs found.")
    else:
        # Perform HTTP requests with different IPs and subdomains
        curl_with_ips(reachable_ips, subdomains_file)
