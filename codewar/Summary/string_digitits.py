Given a string of digits, 
you should replace any digit below 5 with '0' 
and any digit 5 and above with '1'. Return the resulting string.


def fake_bin(x):
    li = list(x)
    lin = list(map(int, li))
    res = []
    for num in lin:
        if num < 5:
            res.append(0)
        else:
            res.append(1)
    restr = ""
    for i in res:
        restr += str(i)
    return restr

print(fake_bin("148564"))
------------------------------------------------------------
def fake_bin(x):
    return ''.join('0' if c < '5' else '1' for c in x)
------------------------------------------------------------    
def fake_bin(x):
    result = ""
    for num in x:
        if int(num) < 5:
            result = result + "0"
        else:
            result = result + "1"
    return result
   
--------------------------------------------------------------
import string

def fake_bin(s):
    return s.translate(string.maketrans('0123456789', '0000011111'))
