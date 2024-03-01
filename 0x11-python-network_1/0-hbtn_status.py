#!/usr/bin/python3
import urllib.request
'''
    script that fetches https://alx-intranet.hbtn.io/status
'''


if __name__ == "__main__":
    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as r:
        body = r.read()
        print("Body response:")
        print("\t- type:", type(body))
        print("\t- content:", body)
        print("\t- utf8 content:", body.decode('utf-8'))
