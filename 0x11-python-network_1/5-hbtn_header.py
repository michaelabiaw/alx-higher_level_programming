#!/usr/bin/python3
"""Displays the X-Request-Id header variable of a request to a given URL
"""
import sys
import requests


if __name__ == "__main__":
    path = sys.argv[1]

    res = requests.get(path)
    print(res.headers.get("X-Request-Id"))
