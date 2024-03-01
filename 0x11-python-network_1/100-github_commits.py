#!/usr/bin/python3
'''
    interview
'''
import requests
import sys


if __name__ == "__main__":
    repo = sys.argv[1]
    username = sys.argv[2]
    url = 'https://api.github.com/repos/{}/{}/commits'.format(username, repo)
    commits = requests.get(url).json()
    try:
        for i in range(10):
            print("{}: {}".format(
                commits[i].requests.get("sha"),
                commits[i].requests.get("commit").
                requests.get("author").requests.get("name")))
    except Exception:
        pass
