#!/usr/bin/python3
'''
    search API
'''
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    q = sys.argv[2]
    response = requests.post(url, {'q': q})
    try:
        data = response.json()
        if data:
            print("[{}] {}".format(data.get('id'), data.get('name')))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
