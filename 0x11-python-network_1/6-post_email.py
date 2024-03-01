#!/usr/bin/python3
'''
    Post an email
'''
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]
    val = {'email': sys.argv[2]}
    resp = requests.post(url, data=val)
    print(resp.text)
