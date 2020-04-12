class A: #经典类
  pass
 
class B(object): #新式类
  pass


在python3中，无论是经典类还是新式类都是广度优先查找。 


----------------------------------------------------------
class Shenxian:
    def fly(self):
        print("神仙都会飞")

class Monkey:
    def eat_peach(self):
        print("猴子都喜欢吃桃子")

class MonkeyKing(Shenxian, Monkey):

    def play_golden_stick(self):
        print("孙悟空玩金箍棒")

sxz = MonkeyKing()
sxz.eat_peach()
sxz.fly()
sxz.play_golden_stick()

/*
猴子都喜欢吃桃子
神仙都会飞
孙悟空玩金箍棒
*/

---------------------------------------------------------
class ShenxianBase:
    def fight(self):
        print("神仙始祖们在天界打架")

class Shenxian(ShenxianBase):
    def fly(self):
        print("神仙都会飞")
    def fight(self):
        print("神仙打架")

class MonkeyBase:
    def fight(self):
        print("猿猴在打架")

class Monkey(MonkeyBase):
    def eat_peach(self):
        print("猴子都喜欢吃桃子")
    def fight(self):
        print("猴子打架")



class MonkeyKing(Shenxian, Monkey):

    def play_golden_stick(self):
        print("孙悟空玩金箍棒")

m = MonkeyKing()
# m.play_golden_stick()
# m.fly()
# m.eat_peach()

m.fight()

#神仙打架
