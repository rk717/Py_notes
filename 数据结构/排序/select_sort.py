# def select_sort_simple(li):
#     li_new = []
#     for i in range(len(li)):
#         min_val = min(li)
#         li_new.append(min_val)
#         li.remove(min_val)
#     return li_new

#不推荐上面的方法，占内存

def select_sort(li):
    for i in range(len(li) - 1): #i是第几趟
        min_loc = i
        for j in range(i, len(li)):
            if li[j] < li[min_loc]:
                min_loc = j 
        li[i], li[min_loc] = li[min_loc], li[i]

# 选择排序（Select Sort）

# 一趟排序记录最小的数，放到第一个位置。
# 再一趟排序记录列表无序区最小的数，放到第二个位置。

# 算法关键点：有序区和无序区，无序区最小数的位置
    