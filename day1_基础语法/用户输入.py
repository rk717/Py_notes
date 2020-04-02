name = input("输入你的名字:")
age = float(input("输入你的年龄:"))
height = input("输入你的身高:")
question = input("你是不是全身都黑:")

#

msg = '''
---------Personal Info----------
Name    : %s
Age     : %f 
Height  : %s
Answer  : %s
----------End-------------------
''' % (name,age,height,question)

print(msg)

if question == "Y" or question == "y":
    print("我不信，让我看看。。。")