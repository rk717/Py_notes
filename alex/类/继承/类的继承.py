主要作用就是节省代码。 

class Animal:
    a_type = "哺乳动物"

    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex
    
    def eat(self):
        print("%s is eating..."% self.name)

class Person(Animal):
    a_type = "高等动物"

    def talk(self):
        print("person %s is talking..." % self.name)
    def eat(self):
        Animal.eat(self)
        print("Human is eating ")

class Dog(Animal):
    def chase_rabbit(self):
        print("%s is chasing the rabbit..." % self.name)

p = Person("Lin", 21, "M")
p.eat()
p.talk()
print(p.a_type)

d = Dog("Mjj", 3, "Female")
d.eat()
d.chase_rabbit()
print(d.a_type)


/*
Lin is eating...
Human is eating
person Lin is talking...
高等动物
Mjj is eating...
Mjj is chasing the rabbit...
哺乳动物
*/
