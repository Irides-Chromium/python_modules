#!/usr/bin/python3

### rev: 5.0
### author: <zhq>
### features:
###     errors included
###     up to 63 scales (2 to 64)
###     using list as joining tool(used as debug)
###     caps recognition and same output format
### for the function parameters, `cur` represents the current (input) base, `res` represents the result (output) base, and `num` represents the current (input) number.

def scale(cur, res, num):
#         int, int, str -> str
# Default Settings
    num = str(num)
    error = iscaps = False
    defined = positive = True

    # Input
    if cur == res: return num
    if num == "0": return "0"
    if cur not in range(2, 65) or res not in range(2, 65):
        raise Exception("Base not defined.")
    if num.count("-") == 1:
        positive = False
        num = num[1:]
    result = 0
    unit = 1

    if cur != 10:
        for i in num[::-1]:
            value = ord(i)
            if value in range(48, 58): value -= 48
            elif value in range(65, 92): value -= 55
            elif value in range(97, 123): value -= 61
            elif value == 64: value = 62
            elif value == 95: value = 63
            assert value <= cur, "Digit larger than original base."
            result += value * unit
            unit *= cur
        result = str(result)

    # Output
    if res != 10:
        num = int(result or num)
        result = ""
        while num > 0:
            value = num % res
            if value < 10: digit = value + 48
            elif value < 36: digit = value + 55
            elif value < 62: digit = value + 61
            elif value == 62: digit = 64
            elif value == 63: digit = 95
            result = chr(digit) + result
            num //= res
    if error: raise Exception("ERROR")
    elif defined:
        if not positive: result = "-" + result
        return result
