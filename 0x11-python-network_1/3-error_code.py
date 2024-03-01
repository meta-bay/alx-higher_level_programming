#!/usr/bin/python3
'''
    Error code
'''
import sys
import urllib.request


if __name__ == "__main__":
    req = urllib.request.Request(sys.argv[1])
    try:
        with urllib.request.urlopen(req) as response:
            body = response.read()
            dec = body.decode('utf-8')
    except urllib.error.HTTPError as e:
        print('Error code:', e.code)
