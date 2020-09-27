Your job is to write a function which increments a string, to create a new string.

If the string already ends with a number, the number should be incremented by 1.
If the string does not end with a number. the number 1 should be appended to the new string.

Test.assert_equals(increment_string("foo"), "foo1")
Test.assert_equals(increment_string("foobar001"), "foobar002")
Test.assert_equals(increment_string("foobar1"), "foobar2")
Test.assert_equals(increment_string("foobar00"), "foobar01")
Test.assert_equals(increment_string("foobar99"), "foobar100")
Test.assert_equals(increment_string("foobar099"), "foobar100")
Test.assert_equals(increment_string(""), "1")




import re

def increment_string(s):
    number = re.findall(r'\d+', s)
    if number:
        s_number = number[-1]
        s = s.rsplit(s_number, 1)[0]
        number = str(int(s_number) + 1)
        return s + '0' * (len(s_number) - len(number)) + number
    return s + '1'
    

--------------------------------------
def increment_string(strng):
    head = strng.rstrip('0123456789')
    tail = strng[len(head):]
    if tail == "": return strng+"1"
    return head + str(int(tail) + 1).zfill(len(tail))
    
--------------------------------------
def increment_string(strng):
    
    # strip the decimals from the right
    stripped = strng.rstrip('1234567890')
    
    # get the part of strng that was stripped
    ints = strng[len(stripped):]
    
    if len(ints) == 0:
        return strng + '1'
    else:
        # find the length of ints
        length = len(ints)
    
        # add 1 to ints
        new_ints = 1 + int(ints)
    
        # pad new_ints with zeroes on the left
        new_ints = str(new_ints).zfill(length)
    
        return stripped + new_ints
