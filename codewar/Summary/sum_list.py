get_sum(1, 0) == 1   // 1 + 0 = 1
get_sum(1, 2) == 3   // 1 + 2 = 3
get_sum(0, 1) == 1   // 0 + 1 = 1
get_sum(1, 1) == 1   // 1 Since both are same
get_sum(-1, 0) == -1 // -1 + 0 = -1
get_sum(-1, 2) == 2  // -1 + 0 + 1 + 2 = 2

def get_sum(a,b):
    if a == b:
        return a
    elif a<b:
        return sum(range(a,b+1))
    elif a>b:
        return sum(range(b,a+1))
        
------------------------------------------
def get_sum(a, b):
    return (a + b) * (abs(a - b) + 1) // 2
    
------------------------------------------
def get_sum(a,b):
    soma=0
    if a==b:
        return a
    elif a > b:
        for i in range(b,a+1):
            soma += i
        return soma
    else:
        for i in range(a,b+1):
            soma += i
        return soma
