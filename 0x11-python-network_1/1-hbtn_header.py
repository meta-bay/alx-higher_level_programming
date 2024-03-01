#!/usr/bin/python3
'''
    Response header value
'''
import sys
import urllib.request


if __name__ == "__main__":
    req = urllib.request.Request(sys.argv[1])
    with urllib.request.urlopen(req) as response:
        req_id = response.headers.get('X-Request-Id')
        print(req_id)
