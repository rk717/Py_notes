def abbrevName(s):
    #code away!
    l = s.split()
    new = ""

    for i in range(len(l)-1):
        s = l[i]
        new += (s[0] + '.')
        a = l[1]
        new += a[0]
    return new
        

print(abbrevName("Lian Yilin"))

#L.Y

------------------------------------------------
def abbrevName(name):
    return name.split(' ')[0][0].upper()+'.'+name.split(' ')[1][0].upper()
    
===================================================
def abbrevName(name):
    x = name
    y = name.split()
    return y[0][0].upper() + "." + y[1][0].upper()
