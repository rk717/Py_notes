def insert_sort(li):
    for i in range(1, len(li)): #i表示摸到的牌的下标
        tmp = li[i]
        j = i - 1 #j指的是手里的牌的下标
        while j >= 0 and li[j] > tmp:
            li[j+1] = li[j]
            j -= 1 #把j的箭头 往 左移动一个位置
        li[j+1] = tmp 
