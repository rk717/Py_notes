在python中，这种一边循环一边计算后面元素的机制，称为生成器。（惰性运算）

如何创建一个生成器generator呢？

1. 只要把一个列表生成式的【】改成（）， 就创建了一个generator。
>>>[x * x for x in range(10)]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

>>>(x * x for x in range(10))
<generator object <genexpt> at 0x101ebc3b8>

(x * x for x in range(10)) 生成的就是一个生成器。

如何打印出generator的每一个元素呢？

可以通过next（）函数获得generator的下一个返回值：

>>>g = (x * x for x in range(10))
>>>next(g)
0
>>>next(g)
1
...
...
...
>>>next(g)
81
>>>next(g)
StopIteration

我们讲过， generator保存的是算法，每次调用next（g）就计算出 g 的下一个元素的值， 直到计算到最后一个值，
没有更多的元素时，跳出StopIteration的错误。

或：

>>>g = (x * x for x in range(10))
>>>for n in g:
...     print(n)
0
1
4
...
...
...
64
81

通过for循环来迭代它，就不需要关心StopIteration的错误了。




