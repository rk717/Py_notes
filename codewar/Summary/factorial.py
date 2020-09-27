n = 23
fact = 1

for i in range(1,n+1): 
	fact = fact * i 
	
print (fact) 

#25852016738884976640000

----------------------------------

import math 

print (math.factorial(23)) 

#25852016738884976640000

----------------------------------
计算数字阶乘中的尾随零
zeros(6) = 1
# 6! = 1 * 2 * 3 * 4 * 5 * 6 = 720 --> 1 trailing zero

zeros(12) = 2
# 12! = 479001600 --> 2 trailing zeros

import math

def zeros(n):
    count = 0
    i = 5
    while(n/i >= 1):
        count += int(n/i)
        i *= 5
    return int(count)
    
print(zeros(30))  #7
        
  

