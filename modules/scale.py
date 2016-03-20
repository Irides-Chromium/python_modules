### Rev: 4.0
### Author: <zhq>
### FEATURES:
###     Errors Included
###     Up to 61 Scales (2 to 62)
###     Using List as Joining Tool(USED AS DEBUG)
###     Caps Recognition and Same Output Format
### For the function parameters, `cur` represents the current (input) base, `res` represents the result (output) base, and `num` represents the current (input) number.

def count(string):
    count = 0
    for i in string:
        count += 1
    return count

def scale(cur, res, num):
# Default Settings
    cur = int(cur)
    res = int(res)
    inmode = 0
    outmode = 0
    CapsFlag = True
    Defined = True
    Out_Of_Index_ERROR = False
    Translation_ERROR = False
    Float = False
    Positive = True

    # From
    if cur > 62 or res > 62: Defined = False
    num = int(num)
    if num.count('.') == 1:
        Float =True
    if num.count('-') == 1:
        Positive = False
    if cur > 36: inmode = 1
    if res > 36: outmode = 1
    l = str(num)
    num = 0
    n = count(l)
    
    if inmode == 1:
        for i in range(0, n):
            try: b = ord(l[i])
            except: Translation_ERROR = True
            if b >= 65 and b <= 91:
                a = b - 29
            elif b >= 97 and b <= 122:
                a = b - 87
            else: a = int(chr(b))
            if a >= cur: Out_Of_Index_ERROR = True
            num += a*int(cur)**(n-i-1)
            num = int(num)
            b = 0
            a = 0
    else:
        for i in range(0, n):
            try: b = ord(l[i])
            except: Translation_ERROR = True
            if b >= 65 and b <= 91:
                a = b - 55
                CapsFlag = True
            elif b >= 97 and b <= 122:
                a = b - 87
                CapsFlag = False
            else: a = int(chr(b))
            if a >= cur: Out_Of_Index_ERROR = True
            num += a*int(cur)**(n-i-1)
            num = int(num)
            b = 0
            a = 0

    # To
    if res != 10:
        l = []
        for i in range(1, 17):
            if int(res)**i > num:
                n = i
                break
        a = 0
        if outmode == 1:
            for i in range(1, n+1):
                a = num%int(res)
                b = a
                if a >= 10 and a <= 35:
                    b = chr(int(a + 87))
                if a >= 36 and a <= 61:
                    b = chr(int(a + 29))
                l = [str(b)] + l
                num = int(num/int(res))
            num = ''.join(l)
        else:
            for i in range(1, n+1):
                a = num%int(res)
                b = a
                if a >= 10 and a <= 35:
                    if CapsFlag == True:
                        b = chr(int(a + 55))
                    if CapsFlag == False:
                        b = chr(int(a + 87))
                l = [str(b)] + l
                num = int(num/int(res))
            num = ''.join(l)
    if Defined == False:
        raise Exception("SCALE_OUT_OF_DEFINED_BOUND");
        return 'INTERGER NOT DEFINED'
    if Translation_ERROR == True:
        raise Exception("CANNOT_CAST_STR_TO_INT");
    if Out_Of_Index_ERROR == True:
        raise Exception("SCALE_OUT_OF_BOUND");
    if Translation_ERROR == False and\
    Out_Of_Index_ERROR == False and\
    Defined == True:
        return num
