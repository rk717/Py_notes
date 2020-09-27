def tribonacci(signature, n):
    tribonacci = []

    for i in range(n):
        new_elm = signature[-1] + signature[-2] + signature[-3]
        signature.append(new_elm)
        elm = signature.pop(0)
        tribonacci.append(elm)
    return tribonacci
    
print(tribonacci([1,1,1],10))  
        
#[1, 1, 1, 3, 5, 9, 17, 31, 57, 105]
