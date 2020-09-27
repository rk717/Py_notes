my_module.py

name = "alex"

print("hello",name)
def sayhi(n):
  print("hi,", n)
  
  
-------------------------------
my_module2.py

import my_module 

my_module.sayhi("jack")

#hello alex
#hello jack


    #模块 模块查找路径有关系
    
