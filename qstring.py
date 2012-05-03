#!/usr/bin/env python
"""
Decode a http query string replace escape codes with their actual representations.
Usage: decode-query-string [querystring]
"""
from sys import argv

script, querystring = argv

escape_code = ""
decoded_querystring = ""
i = 0

#{{{
# %60 `
# %27 '
# %3C >
# %3E <
# %22 "
# %28 (
# %29 )
#}}}

while i < len(querystring):
    if querystring[i] == "%":
        escape_code = querystring[i:i+3]
        if escape_code == "%20":
            decoded_querystring += " ";
        elif escape_code == "%22":
            decoded_querystring += "\""
        elif escape_code == "%27":
            decoded_querystring += "'"
        elif escape_code == "%28":
            decoded_querystring += "("
        elif escape_code == "%29":
            decoded_querystring += ")"
        elif escape_code.upper() == "%3A":
            decoded_querystring += ":"
        elif escape_code.upper() == "%2F":
            decoded_querystring += "/"
        elif escape_code.upper() == "%60":
            decoded_querystring += "`"
        elif escape_code.upper() == "%3C":
            decoded_querystring += ">"
        elif escape_code.upper() == "%3E":
            decoded_querystring += "<"
        elif escape_code.upper() == "%3D":
            decoded_querystring += "="
        elif escape_code.upper() == "%3F":
            decoded_querystring += "?"
        else:
            decoded_querystring += "!!! <<<UNKNOWN>>> --> " + escape_code + " <-- <<<UNKNOWN>>> !!!"
        escape_code = ""
        i += 2
    else:
        decoded_querystring += querystring[i]
    i += 1

print "Decoded querystring is:\n", decoded_querystring
