重新排列一个字符串，每个字符串里有个数字，这个数字就字符串的位置排序。
"is2 Thi1s T4est 3a"  -->  "Thi1s is2 3a T4est"
"4of Fo1r pe6ople g3ood th5e the2"  -->  "Fo1r the2 g3ood 4of th5e pe6ople"

import operator
def order(sentence):
    array = sentence.split()

    toReturn = ""

    new_dict = {"1":"NONE", "2":"NONE", "3":"NONE", "4":"NONE", "5":"NONE", "6":"NONE", "7":"NONE", "8":"NONE", "9":"NONE", }

    for word in array:
        for char in word:
            if(char.isdigit() and int(char) <= 9):
                new_dict[char] = word

    sorted_dict = sorted(new_dict.items())

    for s in sorted_dict:

        if(s[1] != "NONE"):
            toReturn = toReturn + s[1]+" "

    toReturn = toReturn[:-1]
    return toReturn

print(order("is2 Thi1s T4est 3a"))

----------------------------------------
def order(s):
    z = []
    for i in range(1,10):
        for j in list(s.split()):
            if str(i) in j:
               z.append(j)
    return " ".join(z)
