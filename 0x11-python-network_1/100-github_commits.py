#!/usr/bin/python3
'''
    interview
'''
from requests import get
import sys


if __name__ == "__main__":
    repo = sys.argv[1]
    oname = sys.argv[2]
    url = 'https://api.github.com/repos/{}/{}/commits'.format(oname, repo)
    commits = get(url).json()
    try:
        for i in range(10):
            print("{}: {}".format(
                commits[i].get("sha"),
                commits[i].get("commit").get("author").get("name")))
    except Exception:
        pass
