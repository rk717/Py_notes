def findSmallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index

def selectionSort(arr):
    newArr = []
    for i in range(len(arr)):
        smallest = findSmallest(arr)
        newArr.append(arr.pop(smallest))
    return newArr

print(selectionSort([5, 3, 6, 2, 10]))
#[2, 3, 5, 6, 10]

#计算机内存犹如一大堆抽屉
#需要存储多个元素时，可使用数组或链表
#数组的元素都在一起
#链表的元素是分开的，其中每个元素都存储了下一个元素的地址
#数组的读取速度很快
#链表的插入和删除的速度很快
#在同一数组中，所有元素的类型都必须相同（都为int，double，等）