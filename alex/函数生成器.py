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

-----------------------------------------------------------------------
def g_test():
    while True:
        n = yield #收到的值 给n

        print("receive from outside:", n)
g = g_test()
g.__next__() #调用生成器，同时发送None到Yield

for i in range(10):
    g.send(i) #调用生成器，同时发送i
    
#receive from outside: 0

#receive from outside: 1

#receive from outside: 2

.......

#receive from outside: 9
--------------------------------------------------------------
    
用生成器实现并发编程
单线程下的多并发效果，线程就是cpu执行的任务单元。

#吃包子 c1, c2, c3
#生产者

def consumer(name):
    print("消费才%s准备吃包子啦。。"% name)
    while True:
        baozi = yield #接收外面的包子
        print("消费者%s收到包子编号：%s"%(name,baozi))

c1 = consumer("c1")
c2 = consumer("c2")
c3 = consumer("c3")
c1.__next__()
c2.__next__()
c3.__next__()

for i in range(5):
    print("-----------生成了地%s批包子-------"%i)
    c1.send(i)
    c2.send(i)
    c3.send(i)
    
消费才c1准备吃包子啦。。
消费才c2准备吃包子啦。。
消费才c3准备吃包子啦。。
-----------生成了地0批包子-------
消费者c1收到包子编号：0
消费者c2收到包子编号：0
消费者c3收到包子编号：0
-----------生成了地1批包子-------
消费者c1收到包子编号：1
消费者c2收到包子编号：1
消费者c3收到包子编号：1
-----------生成了地2批包子-------
消费者c1收到包子编号：2
消费者c2收到包子编号：2
消费者c3收到包子编号：2
-----------生成了地3批包子-------
消费者c1收到包子编号：3
消费者c2收到包子编号：3
消费者c3收到包子编号：3
-----------生成了地4批包子-------
消费者c1收到包子编号：4
消费者c2收到包子编号：4
消费者c3收到包子编号：4

 

