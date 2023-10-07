import re
import requests
import argparse

def is_valid_endpoint(endpoint):
    # Define a regular expression pattern to match valid endpoints
    valid_endpoint_pattern = r'^(https?://[^\s/$.?#][^\s]*)|(/[\w-]+(?:/[\w-]+)*)$'
    
    # Check if the endpoint contains characters like "
    if re.search(r'["\']', endpoint):
        return False
    
    return re.match(valid_endpoint_pattern, endpoint) is not None

def extract_endpoints_from_url(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        content = response.text

        # Define a regular expression pattern to match specific endpoints
        pattern = r'(https?://[^\s/$.?#][^\s]*)|(/[\w-]+(?:/[\w-]+)*)'

        # Use regular expression to find specific endpoints in the content
        endpoints = re.findall(pattern, content)

        # Filter out empty matches and flatten the list
        endpoints = [match[0] if match[0] else match[1] for match in endpoints if not re.search(r'["\']hacker["\']', match[0])]

        # Further exclude endpoints containing "support-tools"
        endpoints = [endpoint for endpoint in endpoints if "support-tools" not in endpoint]

        # Filter out invalid endpoints
        endpoints = [endpoint for endpoint in endpoints if is_valid_endpoint(endpoint)]

        # Remove duplicates by converting the list to a set and back to a list
        endpoints = list(set(endpoints))

        return endpoints
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None

def save_endpoints_to_file(endpoints, output_file):
    if not endpoints:
        print("No endpoints to save.")
        return
    
    try:
        with open(output_file, 'w') as file:
            for endpoint in endpoints:
                file.write(endpoint + '\n')
        print(f"Endpoints saved to {output_file}")
    except IOError as e:
        print(f"Error while saving endpoints: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Extract endpoints from a URL and optionally save them to a file.")
    parser.add_argument("url", help="URL to extract endpoints from")
    parser.add_argument("-o", "--output", help="Output file to save endpoints")

    args = parser.parse_args()
    url = args.url
    output_file = args.output

    endpoints = extract_endpoints_from_url(url)

    if endpoints:
        print("Endpoints found:")
        for endpoint in endpoints:
            print(endpoint)

        if output_file:
            save_endpoints_to_file(endpoints, output_file)
