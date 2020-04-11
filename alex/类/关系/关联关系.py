class Person:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex
        self.partner = None #应该是一个对象，代表 另一半

    def do_private_stuff(self):
        pass

p1 = Person("Mjj", 24, "M")
p2 = Person("Lyy", 22, "F")

#双向绑定，关联
p1.partner = p2 #这样就把Lyy当作了Mjj的另一半
p2.partner = p1

print(p1.partner.name, p2.partner.name)


#Lyy Mjj
