class Person(object):
    def __init__(self, name, age):
        self.name = name     #实例变量， 成员变量， 实例属性
        self.age = age
        self.__life_val = 100  #私有变量， 私有属性
    
    def get_life_val(self):
        print("life still has ", self.__life_val)
        return self.__life_val
    
    def __breath(self): #只能自己访问
        print("%s is breathing.." %self.name)

    def get_attack(self):
        self.__life_val -= 20
        print("被攻击了， 生命值减20")
        self.__breath()
        return self.__life_val

a = Person("alex", 22)

#print(a.life_val) #外部无法访问，已封装。

a.get_life_val() #只能从内部访问
a.get_attack()

#a.__breath() #不可以访问 

#特例，强行访问， 实例名._类名+方法名()  , 对封装的破解
a._Person__breath()


a._Person__life_val = 10  #修改私有属性
a.get_life_val()

a.__val = 444 #实例生成后，再创建的私有属性，并不具有私有性， 是可以直接访问的。
print(a.__val)

/*
life still has  100
被攻击了， 生命值减20
alex is breathing..
alex is breathing..
life still has  10
444
*/
