{"Java": 10, "Ruby": 80, "Python": 65}    -->  ["Ruby", "Python"]
{"Hindi": 60, "Dutch" : 93, "Greek": 71}  -->  ["Dutch", "Greek", "Hindi"]
{"C++": 50, "ASM": 10, "Haskell": 20}     -->  []

def my_languages(dict):
    store = []
    for key, value in dict.items():
        if value >= 60:
            store.append(key)
    return sorted(store, key=lambda x: dict[x], reverse= True)
    
--------------------------------------------------

from collections import OrderedDict


def my_languages(d):
    d = OrderedDict(sorted(d.items(), key = lambda kv:(kv[1],kv[0])))    
    a = []
    d = dict((k,v) for k, v in d.items() if v >= 60)
    for key in d.keys():
        a.append(key)
        
    a.reverse()
    return a
print(my_languages({"Hindi": 60, "Dutch": 93, "Greek": 71}))
