li = [(1, 2), (3, 4), (5, 6)]
for i,h in li:
print(i, h)
#1 2
#3 4
#5 6

li = [(1,2), (3,4), (5,6)]
for i in li:
    print (i)
#(1, 2)
#(3, 4)
#(5, 6)

l1 = [1,2,3]
l2 = [4,5,6]
for i,h in zip(l1, l2):
    print(i,h)
#1 4
#2 5
#3 6
