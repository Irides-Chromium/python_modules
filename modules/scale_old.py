#!/usr/bin/python3
### rev: 4.0
### author: <zhq>
### features:
###     errors included
###     up to 61 scales (2 to 62)
###     using list as joining tool(used as debug)
###     caps recognition and same output format
### for the function parameters, `cur` represents the current (input) base, `res` represents the result (output) base, and `num` represents the current (input) number.

def scale(cur, res, num):
# default settings
    cur = int(cur)
    res = int(res)
    inmode = False
    outmode = False
    caps = True
    defined = True
    out_of_index = False
    trans_error = False
    _float = False
    positive = True

    # from
    if cur > 64 or res > 64: defined = False
    l = str(num)
    if l.count('.') == 1: _float = True
    if l.count('-') == 1: positive = False
    if cur > 36: inmode = True
    if res > 36: outmode = True
    num = 0
    n = len(l)
    
    if inmode == True:
        for i in range(0, n):
            try: b = ord(l[i])
            except: trans_error = True
            if b >= 65 and b <= 91: a = b - 29
            elif b >= 97 and b <= 122: a = b - 87
            elif b == 64: a = 62            # '@'
            elif b == 95: a = 63            # '_'
            else: a = int(chr(b))
            if a >= cur: out_of_index = True
            num += a * int(cur) ** (n - i - 1)
            num = int(num)
            b = 0
            a = 0
    else:
        for i in range(0, n):
            try: b = ord(l[i])
            except: trans_error = True
            if b >= 65 and b <= 91:
                a = b - 55
                caps = True
            elif b >= 97 and b <= 122:
                a = b - 87
                caps = False
            else: a = int(chr(b))
            if a >= cur: out_of_index = True
            num += a * int(cur) ** (n - i - 1)
            num = int(num)
            b = 0
            a = 0

    # to
    if res != 10:
        l = []
        for i in range(1, 17):
            if int(res) ** i > num:
                n = i
                break
        a = 0
        if outmode == True:
            for i in range(1, n+1):
                a = num % int(res)
                b = a
                if a >= 10 and a <= 35: b = chr(int(a + 87))
                elif a >= 36 and a <= 61: b = chr(int(a + 29))
                elif a == 62: b = "@"
                elif a == 63: b = "_"
                l = [str(b)] + l
                num = int(num / int(res))
            num = ''.join(l)
        else:
            for i in range(1, n + 1):
                a = num % int(res)
                b = a
                if a >= 10 and a <= 35:
                    if caps == True: b = chr(int(a + 55))
                    if caps == False: b = chr(int(a + 87))
                l = [str(b)] + l
                num = int(num / int(res))
            num = ''.join(l)
    if defined == False:
        raise Exception("SCALE_OUT_OF_DEFINED_BOUND");
    if trans_error == True:
        raise Exception("CANNOT_CAST_STR_TO_INT");
    if out_of_index == True:
        raise Exception("SCALE_OUT_OF_BOUND");
    if trans_error == False \
    and out_of_index == False \
    and defined == True:
        return num
