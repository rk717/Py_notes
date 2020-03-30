generator 非常强大，如果推算的算法比较复杂，用类似列表生成式的for循环无法实现的时候，
还可以用函数来实现。

比如著名的Fibonacci数列。
a = 0
b = 1
count = 0
while count < 20:
    tmp = a #给新的a赋值前，先把旧值存下来
    a = b  # 新的a=1
    b = tmp + b #
    print(b)
    count += 1
-------------------------------------    
 def fib(n):
    a = 0
    b = 1
    count = 0
    while count < n:
        tmp = a #给新的a赋值前，先把旧值存下来
        a = b  # 新的a=1
        b = tmp + b #
        print(b)
        count += 1

fib(20)


上面的函数和generator仅一步之遥， 要把fib函数变成generator，
只需要把print(b)改为yield b 就可以了。
def fib(n):
    a = 0
    b = 1
    count = 0
    while count < n:
        tmp = a #给新的a赋值前，先把旧值存下来
        a = b  # 新的a=1
        b = tmp + b #
        #print(b)
        yield b #暂停 类似与return， return是整个函数结束，yield是暂停。
        count += 1
fib(20)
