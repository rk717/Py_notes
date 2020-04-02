Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks untouched

pig_it('Pig latin is cool') # igPay atinlay siay oolcay
pig_it('Hello world !')     # elloHay orldway !

import re
def pig_it(text):
    #your code here
    regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]') 
    if(regex.search(text) == None):
        li = text.split(" ")
        li2 = [word[1:] + word[0:1] for word in li]
        li3 = [word + 'ay' for word in li2]
        return (' '.join(li3))
    else:
        li = text.split(" ")
        li2 = [word[1:] + word[0:1] for word in li]
        li3 = [word + 'ay' for word in li2[:-1]]
        
        res = (' '.join(li3)) +" " + li[-1]
        return res
        
    
    # li2 = [word[::-1] for word in li]
    # res = [word + 'ay' for word in li2]
    # return res
print(pig_it('Quis custodiet ipsos custodes ?'))
#'hisTay siay ymay tringsay'

# def pig_it(text):
#     #your code here
#     li = text.split(" ")
#     li2 = [word[::-1] for word in li]
#     res = [word + 'ay' for word in li2]
#     return res


简单方法：
def pig_it(text):
    lst = text.split()
    return ' '.join([word[1:] + word[:1] + 'ay' if word.isalpha() else word for word in lst])
            #hello   ello           h
print(pig_it("hello its me"))
