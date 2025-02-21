#! /usr/bin env python3
import argparse
import requests

def scan_domain(domain):
    print(f"Scanning domain: {domain}")
    response = requests.get(f"https://{domain}")
    print(f"Status Code: {response.status_code}")
    print(response.text)

def main():
    parser = argparse.ArgumentParser(description="DataSploit")
    parser.add_argument("--domain", help="Domain name to scan")
    args = parser.parse_args()
    
    if args.domain:
        scan_domain(args.domain)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()

