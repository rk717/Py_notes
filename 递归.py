#100/2 = 50
#50 /2 = 25

用while循环实现： 
n = 100
while n > 0:
  n = int(n / 2)
  print(n)
  
  
用递归实现：

def calc(n):
  print(n)
  n = int (n/2) #50
  if n > 0:
    calc(n)  # n = 50, 执行完之后， 又调用自己的函数，继续执行， 实现递归。
  
