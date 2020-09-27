# 冒泡排序（Bubble Sort）
# 列表每个相邻的数，如果前面比后面大，则交换这两个数。
# 一趟排序完成后，则无序区减少一个数，有序去增加一个数。

import random

def bubble_sort(li):
    for i in range(len(li) - 1): #第i趟
        exchange = False  #exchange 来记录列表是否改变
        for j in range(len(li) - i - 1):
            if li[j] > li[j+1]:
                li[j], li[j+1] = li[j+1], li[j]
        print(li)
        if not exchange:  #如果列表没有改变，则意味着已经排完序，可以结束程序了
            return 



li = [random.randint(0, 10000) for i in range(10)]

print(li)

bubble_sort(li)

print(li)