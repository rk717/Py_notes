class Animal:
    a_type = "哺乳动物"

    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex
        print("---父类的执行方法---")
    
    def eat(self):
        print("%s is eating..."% self.name)

class Person(Animal):
    a_type = "高等动物"

    def __init__(self, name, age, sex, hobby):
        # Animal.__init__(self, name, age, sex)
        #super(Person,self).__init__(name, age, sex)
        super().__init__(name, age, sex) #跟上面这行supper语法的效果一样，一般用这种写法的多
        #用super和上面 Animal.__init__的方法是一样的
        self.hobby = hobby
        print("---子类的执行方法---")

    def talk(self):
        print("person %s is talking..." % self.name)
    
    def eat(self):
        #Animal.eat(self)
        super().eat() #执行父类的方法
        print("Human is eating ")



p = Person("Lin", 21, "M", "Sad")

print(p.name, p.sex, p.hobby)

/*
---父类的执行方法---
---子类的执行方法---
Lin M Sad
*/
