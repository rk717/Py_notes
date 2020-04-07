quote = "How can mirrors be real if our eyes aren't real"
test.assert_equals(to_jaden_case(quote), "How Can Mirrors Be Real If Our Eyes Aren't Real")

Not Jaden-Cased: "How can mirrors be real if our eyes aren't real"
Jaden-Cased:     "How Can Mirrors Be Real If Our Eyes Aren't Real"

def toJadenCase(string):        
    return " ".join(w.capitalize() for w in string.split())
    
=================================================================
import string

def toJadenCase(NonJadenStrings):
    return string.capwords(NonJadenStrings)
    
=================================================================
def toJadenCase(string):
    # ...
    sentence = ''
    words = []
    st = string.split()
    for i in st:
        il = list(i)
        il[0] = il[0].upper()
        words.append(''.join(il))
    return ' '.join(words)
