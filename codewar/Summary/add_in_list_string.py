Test.assert_equals(points(['1:0','2:0','3:0','4:0','2:1','3:1','4:1','3:2','4:2','4:3']), 30)
Test.assert_equals(points(['1:1','2:2','3:3','4:4','2:2','3:3','4:4','3:3','4:4','4:4']), 10)
Test.assert_equals(points(['0:1','0:2','0:3','0:4','1:2','1:3','1:4','2:3','2:4','3:4']), 0)
Test.assert_equals(points(['1:0','2:0','3:0','4:0','2:1','1:3','1:4','2:3','2:4','3:4']), 15)
Test.assert_equals(points(['1:0','2:0','3:0','4:4','2:2','3:3','1:4','2:3','2:4','3:4']), 12)
if x>y - 3 points
if x<y - 0 point
if x=y - 1 point

def points(games):
    n = 0
    for i in games:
        temp = i.split(":")
        n1 = temp[0]
        n2 = temp[1]
        if n1 > n2:
            n += 3
        elif n1 == n2:
            n += 1
    return n
