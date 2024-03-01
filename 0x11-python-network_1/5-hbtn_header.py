#!/usr/bin/python3
'''
    X-Request-Id
'''
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]
    req = requests.get(url)
    req_id = req.headers.get('X-Request-Id')
    print(req_id)
