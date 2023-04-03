#!/usr/bin/python3
"""A script that:
- takes in a URL,
- sends a request to the URL and displays the value
- of the X-Request-Id variable found in the header ofthe response.
"""
import sys
import urllib.request

if __name__ == "__main__":
    path = sys.argv[1]

    res_data = urllib.request.Request(path)
    with urllib.request.urlopen(res_data) as response:
        dict_data = dict(response.headers)
        print(dict_data["X-Request-Id"])
