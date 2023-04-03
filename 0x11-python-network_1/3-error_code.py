#!/usr/bin/python3
"""A script that:
- takes in a URL,
- sends a request to the URL
- displays the body of the response (decoded in utf-8).
"""


if __name__ == "__main__":
    import sys
    from urllib import request, error
    var = sys.argv[1]

    try:
        with request.urlopen(var) as response:
            print(response.read().decode('UTF-8'))
    except error.HTTPError as error:
        print('Error code:', error.code)
