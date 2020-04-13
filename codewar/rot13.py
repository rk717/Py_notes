test.assert_equals(rot13("test"),"grfg")
test.assert_equals(rot13("Test"),"Grfg")


import codecs

def rot13(s):
    return codecs.encode(s, 'rot_13')
    
-----------------
import string

def rot13(message):
    return message.encode("rot13")
