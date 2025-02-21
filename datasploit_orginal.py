#!/usr/bin/env python3

import requests
import argparse

def main():
    print("Running datasploit.py")
    response = requests.get("https://example.com")
    print(response.text)

if __name__ == "__main__":
    main()

