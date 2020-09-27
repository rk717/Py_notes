class Dog:
    d_type = "京巴" #属性，类属性，类变量
    
    def sayhi(self):  #方法，第一个参数必须是 self 代表实例本身
        print("Hello, my name is ",self.d_type)

#实例化
d = Dog() #生成了一个实例
d2 = Dog() #可以生成多个实例

d.sayhi() #实例，方法
d2.sayhi()

print(d.d_type)

