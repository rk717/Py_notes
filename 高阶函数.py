什么是高阶函数？
  1.接受一个或多个函数作为输入。
  2.return返回另一个函数。
  
例如： 

def get_abs(n):
  if n < 0:
    n = int(str(n).strip("-"))
  return n

def add(x,y,f):        # f means the get_abs function
  return f(x) + f(y)
  
res = add(3, -6, get_abs)

print(res)
