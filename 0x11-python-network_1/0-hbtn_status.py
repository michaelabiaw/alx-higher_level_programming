#!/usr/bin/python3
"""A script that
- fetches https://alx-intranet.hbtn.io/status.
- uses urlib.resquest package
"""


if __name__ == '__main__':
    import urllib.request

    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as request:
        data_file = request.read()
        print("Body response:")
        print("\t- type: {}".format(type(data_file)))
        print("\t- content: {}".format(data_file))
        print("\t- utf8 content: {}".format(data_file.decode('utf-8')))
