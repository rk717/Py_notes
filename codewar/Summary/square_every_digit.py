test.assert_equals(square_digits(9119), 811181)

def square_digits(num):
    a = ''.join(str(int(i)**2) for i in str(num))
    return int(a)
    
def square_digits(num):
    ret = ""
    for x in str(num):
        ret += str(int(x)**2)
    return int(ret)
