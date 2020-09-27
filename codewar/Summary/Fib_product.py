求哪两个fib数相乘等于 n

test.assert_equals(productFib(4895), [55, 89, True])
test.assert_equals(productFib(5895), [89, 144, False])
--------------------------------------------------------------

def productFib(prod):
  a, b = 0, 1
  while prod > a * b:
    a, b = b, a + b
  return [a, b, prod == a * b]
  
-------------------------------
def productFib(prod):
    a, b = 0, 1
    rez = 0
    while rez < prod:
        a, b = b, a + b
        rez = a*b
    return [a, b, rez == prod]
    
---------------------------------
def fib(n):
    a,b = 1, 1

    for i in range(n-1):
        a,b = b, a+b
    return a

def productFib(prod):
    if prod == 0:
        return [0, 0, True]
    else:
        current_value = 0
        x = 0
        fib1 = fib2 = 0

        while current_value < prod:
            x += 1
            fib1 = fib(x)
            fib2 = fib(x+1)
            current_value = fib1 * fib2

        if current_value == prod:
            return [fib1, fib2, True]
        return [fib1, fib2, False]


print(productFib(4895))

-------------------------------------------------
求fib数 的 和

def sum_fib(m):
    
    fibo = [0] * (m+1)
    fibo[1] = 1

    sm = fibo[0] + fibo[1]

    for i in range (2, m+1):
        fibo[i] = fibo[i-1] + fibo[i-2]
        sm += fibo[i]
    return sm
