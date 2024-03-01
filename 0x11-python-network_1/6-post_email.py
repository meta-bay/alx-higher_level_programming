#!/usr/bin/python3
'''
    Post an email
'''
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    value = {'email': email}
    response = requests.post(url, data=value)
    print(response.text)
