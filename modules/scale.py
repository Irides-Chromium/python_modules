#!/usr/bin/python3

### rev: 5.0
### author: <zhq>
### features:
###     errors included
###     up to 61 scales (2 to 62)
###     using list as joining tool(used as debug)
###     caps recognition and same output format
### for the function parameters, `cur` represents the current (input) base, `res` represents the result (output) base, and `num` represents the current (input) number.

def scale(cur, res, num):
# Default Settings
    from math import floor
    cur = int(cur)
    res = int(res)
    num = str(num)
    error = iscaps = False
    defined = positive = True

    # Input
    if cur > 64 or res > 64: defined = False
    if num.count("-") == 1:
        positive = False
        num = num[1:]
    inmode = True if cur > 36 else False
    outmode = True if res > 36 else False
    result = 0
    num_of_digit = len(num)

    if cur != 10:
        for i in range(num_of_digit):
            try: value = ord(num[i])
            except: error = True
            if value >= 48 and value <= 57: value -= 48
            elif value >= 97 and value <= 122: value -= 87
            elif inmode:
                if value >= 65 and value <= 91: value -= 29
                elif value == 64: value = 62
                elif value == 95: value = 63
            elif value >= 65 and value <= 91: value -= 55
            if value >= cur: error = True
            result += value * cur ** (num_of_digit - i - 1)
            value = 0

    # Output
    if res != 10:
        num = int(result or num)
        result = ""
        value = 0
        while num > 0:
            value = num % res
            if value < 10: digit = chr(value + 48)
            elif value <= 35: digit = chr(value + 87)
            elif outmode:
                if value <= 61: digit = chr(value + 29)
                elif value == 62: digit = '@'
                elif value == 63: digit = '_'
            elif iscaps: digit = chr(value + 55)
            result = digit + result
            num = floor(num / res)
    if error: raise Exception("ERROR")
    elif defined == True:
        if not positive: num = "-" + str(num)
        return result
