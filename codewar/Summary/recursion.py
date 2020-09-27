def halving_sum(n): 
    
    a = []
    b = n
    while (n > 0):
        a.append(int(n/2))
        n = int(n/2)
    return sum(a) + b

print(halving_sum(25))

#25  =>  25 + 12 + 6 + 3 + 1 = 47
