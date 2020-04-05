def find_smallest_int(arr):
    smallest = []
    for i in range(0, len(arr)):
        if (arr[i] < smallest):
            smallest = arr[i]
    return smallest

def findSmallestInt(arr):
    min = arr[0]
    for item in arr:
        if min > item:
            min = item
    return min
