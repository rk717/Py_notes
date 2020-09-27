def find_uniq(arr):
    arr.sort()

    if(arr[0] < arr[len(arr)-1] and arr[0] < arr[len(arr) - 2]):
        n = arr[0]
    else:
        n = arr[len(arr)-1]

    return n

print(find_uniq([ 1, 1, 1, 2, 1, 1 ]))

# def find_uniq(arr):
#     s = set(arr)
#     for e in s:
#         if arr.count(e) == 1:
#             return e

#https://www.codewars.com/kata/585d7d5adb20cf33cb000235/python