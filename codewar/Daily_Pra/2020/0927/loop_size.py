def loop_size(n):
    l = []
    while not n in l:
        l.append(n)
        n = n.next
    return len(l) - l.index(n)

#https://www.codewars.com/kata/52a89c2ea8ddc5547a000863/python