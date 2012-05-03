#!/usr/bin/env python
# -*- coding: UTF-8 -*-
""" querystringtool

NOTE: DO NOT USE THIS MODULE:
NOTE: Instead, use the module 'decode_query_string', it is more complete and better
writter.

Decode a http query string replace escape codes with their actual
representations.

Usage: querystringtool [querystring]

Copyright (c) Eric M. Kiara 2012
by Eric KIARA(eric@eric.co.ke)
Created 2012-02-15
"""
from sys import argv

querystring = arg[1]


def main():
    """ main
    """
    decoded_querystring = ""
    i = 0

    while i < len(querystring):
        escape_code = ""
        if querystring[i] == "%":
            escape_code = querystring[i:i + 3]
            if escape_code == "%20":
                decoded_querystring += " "
            elif escape_code.upper() == "%2F":
                decoded_querystring += "/"
            elif escape_code == "%22":
                ###decoded_querystring += "\""
                decoded_querystring += '"'
            elif escape_code == "%23":
                decoded_querystring += "<XXXX>"
            elif escape_code == "%24":
                decoded_querystring += "<XXXX>"
            elif escape_code == "%25":
                decoded_querystring += "<XXXX>"
            elif escape_code == "%26":
                ###decoded_querystring += "<XXXX>"
                decoded_querystring += "+"
            elif escape_code == "%27":
                decoded_querystring += "'"
            elif escape_code == "%28":
                decoded_querystring += "("
            elif escape_code == "%29":
                decoded_querystring += ")"
            elif escape_code.upper() == "%60":
                decoded_querystring += "`"
            elif escape_code.upper() == "%3A":
                decoded_querystring += ":"
            elif escape_code.upper() == "%3B":
                decoded_querystring += "<XXXX>"
            elif escape_code.upper() == "%3C":
                decoded_querystring += ">"
            elif escape_code.upper() == "%3D":
                decoded_querystring += "="
            elif escape_code.upper() == "%3E":
                decoded_querystring += "<"
            elif escape_code.upper() == "%3F":
                decoded_querystring += "?"
            else:
                decoded_querystring += "\n<<<<UNKNOWN>>>>\n"
                decoded_querystring += escape_code 
                decoded_querystring += "\n<<<<UNKNOWN>>>>\n"
            i += 2
        else:
            decoded_querystring += querystring[i]
        i += 1

    print "Decoded querystring is:\n", decoded_querystring


if __name__ == "__main__":
    main()
