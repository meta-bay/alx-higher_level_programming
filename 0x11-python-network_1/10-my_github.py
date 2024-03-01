#!/usr/bin/python3
'''
    my github
'''
import requests
import sys


if __name__ == '__main__':
    url = "http://api.github.com/user"
    username = sys.argv[1]
    passwd = sys.argv[2]
    response = requests.get(url, auth=(username, passwd))
    print(response.json().get('id'))
