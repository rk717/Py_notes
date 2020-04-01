from collections import Counter
def int_diff(arr):
    counts = Counter(arr)
    return counts
print(int_diff([1,1,1,4,3,3,6,2,3,2]))

Counter({1: 3, 3: 3, 2: 2, 4: 1, 6: 1})
