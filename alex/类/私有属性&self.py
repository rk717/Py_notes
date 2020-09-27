class Dog:
    d_type = "京巴" #属性，类属性，类变量 公共属性

    def __init__(self, name, age): #初始化方法，构造函数，实例化时会自动执行，进行一些初始化工作。
        print("hahah", name, age)

    def sayhi(self):  #方法，第一个参数必须是 self 代表实例本身
        print("Hello, my name is ",self.d_type)

#实例化
d = Dog("mjj",3) #生成了一个实例
d2 = Dog("gb",2) #可以生成多个实例

d.sayhi() #实例，方法
d2.sayhi()

print(d.d_type)

/*
hahah mjj 3
hahah gb 2
Hello, my name is  京巴
Hello, my name is  京巴
京巴
*/

-------------------------------------------------------------
class Dog:
    d_type = "京巴" #属性，类属性，类变量 公共属性

    def __init__(self, name, age): #初始化方法，构造函数，实例化时会自动执行，进行一些初始化工作。
        print("hahah", name, age)
        #要想把name，age这两个值，真正的存到实例里，
        #那就要把两个值和实例绑定。
        self.name2 = name #绑定参数值 到实例 d2.name2 = name
        self.age2 = age

    def sayhi(self):  #方法，第一个参数必须是 self 代表实例本身
        print("Hello, my name is ",self.d_type, self.name2)

#实例化
d = Dog("mjj",3) #生成了一个实例
d2 = Dog("gb",2) #可以生成多个实例

d.sayhi() #实例，方法
d2.sayhi() #d2.sayhi(d2)

print(d.d_type)

/*
hahah mjj 3
hahah gb 2
Hello, my name is  京巴 mjj
Hello, my name is  京巴 gb
京巴
*/

self代表实例本身。
