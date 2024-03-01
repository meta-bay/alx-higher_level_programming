#!/usr/bin/python3
'''
    Response header value
'''
import sys
import urllib.request


if __name__ == "__main__":
    with urllib.request.urlopen(sys.argv[1]) as response:
        req_id = response.headers.get('X-Requested-ID')
        print(req_id)
