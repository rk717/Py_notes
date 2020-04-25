def openOrSenior(data):
    a = []
    for i in data:       
        if i[0] > 54 and i[1] > 7:
            a.append("Senior")
        else:
            a.append("Open")
    return a

print((openOrSenior([[45, 12],[55,21],[19, -2],[104, 20]])))

#['Open', 'Senior', 'Open', 'Senior']


------------------------------------------------------------
[[10,0],[3,5],[5,8]]
一串list 里 的list 第一个数的和 减去 第二个数
def number(bus_stops):
  a = 0
  b = 0
  for i in bus_stops:
    a += i[0]
    b += i[1]
  return a - b

-----------------------------------------------------
def number(bus_stops):
    return sum([stop[0] - stop[1] for stop in bus_stops])
