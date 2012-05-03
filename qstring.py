#!/usr/bin/env python
# -*- coding: UTF-8 -*-
""" decode_query_string

Decode a http query string replace escape codes with their actual
character representations.

usage: decode_query_string 'http://example.com/space%20separated%20path/'
'http://example.com/space separated path/'

Copyright (c) Eric M. Kiara 2012
by Eric KIARA(eric@eric.co.ke)
Created 2012-02-15
"""
import sys
import urllib
QUERY_STRING = sys.argv[1]

def main():
    """main
    """
    decoded_query_string = urllib.unquote(QUERY_STRING)
    print decoded_query_string

if __name__ == "__main__":
    main()
