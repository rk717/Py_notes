test.assert_equals(disemvowel("This website is for losers LOL!"),
                              "Ths wbst s fr lsrs LL!")


import re
def disemvowel(string):
    return (re.sub("[aeiouAEIOU]","",string))
    
    
def disemvowel(s):
    for i in "aeiouAEIOU":
        s = s.replace(i,'')
    return s
