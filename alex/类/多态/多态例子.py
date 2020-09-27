多态 （polymorphism) 多个对象共用一个接口。   一个接口，多个表现方式。

class Dog(object):
    def sound(self):
        print("汪汪汪")

class Cat(object):
    def sound(self):
        print("喵喵喵")

def make_sound(animal_obj):
    #统一调用接口
    animal_obj.sound() #不管你进来是什么动物， 我都调用sound方法。

d = Dog()
c = Cat()

make_sound(d)
make_sound(c)

/*
汪汪汪
喵喵喵
*/

--------------------------------------------------------------------
class Document:
    def __init__(self, name):
        self.name = name
    
    def show(self):
        raise NotImplementedError("Subclass must abstract method") #异常处理

class Pdf(Document):
    def show(self):
        return "Show pdf contents"

class Word(Document):
    def show(self):

        return "show word contents"

pdf_obj = Pdf("嫩模联系方式.pdf")
print(pdf_obj.show())

/*
Show pdf contents
*/

-------------------------------------------------------------------------------
class Document:
    def __init__(self, name):
        self.name = name
    
    def show(self):
        raise NotImplementedError("Subclass must abstract method") #异常处理

class Pdf(Document):
    def show(self):
        return "Show pdf contents"

class Word(Document):
    def show(self):

        return "show word contents"

pdf_obj = Pdf("嫩模联系方式.pdf")
word_obj = Word("护士联系方式.pdf")

objs = [pdf_obj, word_obj]
for o in objs:
    print(o.show())
    
/*
Show pdf contents
show word contents
*/
