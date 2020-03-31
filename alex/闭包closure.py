def outer():
    name = "study hard for the future"
    
    def inner():
        print("inner", name)
    return inner                            #注意！！这里只是返回inner的内存地址，并未执行。

func = outer()                              #return the address of inner  <function outer, <locals?.inner at 0x1027621e0>

print(func())                               #相当于执行的是inner()  //inner study hard for the future


注意此时outer已经执行完毕， 正常情况下outer里的内存都已经释放了， 但此时由于闭包的存在，我们却还可以调用inner，并且inner内部还调用了上一层outer里的name变量。 这种黏糊糊的现象就叫做闭包。

闭包的意义： 返回的函数对象，不仅仅是一个函数对象，在该函数外还包裹了一层作用域，这使得，该函数无论在何处调用， 优先使用自己外层包裹的作用域。
