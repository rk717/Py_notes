def count_sheep(n):
    # your code
    
    s = ''
    
    for i in range(1,n+1,1):
        if i < n+1:
            m = ("%s sheep..."%(i))
            s += m
            
            
    return s
-----------------------------------------
def count_sheep(n):
    sheep=""
    for i in range(1, n+1):
        sheep+=str(i) + " sheep..."
    return sheep
----------------------------------------
def count_sheep(n):
    return "".join("{} sheep...".format(i) for i in range(1, n+1))
