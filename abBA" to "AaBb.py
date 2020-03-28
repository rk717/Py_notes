Test.describe("Basic tests")

Test.assert_equals(find_children("abBA"),"AaBb")

Test.assert_equals(find_children("AaaaaZazzz"),"AaaaaaZzzz")

Test.assert_equals(find_children("CbcBcbaA"),"AaBbbCcc")

Test.assert_equals(find_children("xXfuUuuF"),"FfUuuuXx")

Test.assert_equals(find_children(""),"")


def find_children(s):
    a = ''.join(sorted(s))
    b = ''.join(sorted(a,key = str.lower))
    return b
            
print(find_children("abBAdcDC"))

def find_children(pattern):
    return ''.join(sorted(pattern, key=lambda letter: (letter.upper(), letter.islower())))
