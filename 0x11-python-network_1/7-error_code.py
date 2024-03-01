#!/usr/bin/python3
'''
    Error code
'''
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]
    response = requests.get(url)
    if response.status_code != requests.code.ok:
        print('Error code:', response.status_code)
    else:
        print(response.text)
