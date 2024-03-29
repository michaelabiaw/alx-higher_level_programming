#!/usr/bin/python3
"""A script that:
- takes in a URL
- sends a POST request to the passed URL
- takes email as a parameter
- displays the body of the response
"""
import sys
import urllib.parse
import urllib.request


if __name__ == "__main__":
    path = sys.argv[1]
    email = {"email": sys.argv[2]}
    data_email = urllib.parse.urlencode(email).encode("ascii")

    request = urllib.request.Request(path, data_email)
    with urllib.request.urlopen(request) as response:
        print(response.read().decode("utf-8"))
