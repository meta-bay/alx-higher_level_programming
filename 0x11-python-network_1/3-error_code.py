#!/usr/bin/python3
'''
	Error code
'''
import sys
import urllib.request


if __name__ == "__main__":
	req = urllib.request.Request(sys.argv[1])
	try:
		urllib.request.urlopen(req)
	except urllib.error.HTTPError as e:
		print('Error code: ', e.code)
