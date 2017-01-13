#!/usr/bin/python3

import re, sys

print(re.sub("%\w\w%\w\w%\w\w", lambda a:bytearray([int(a.group(0)[i+1:i+3], 16) for i in range(0, 9, 3)]).decode(), sys.stdin.read()))
