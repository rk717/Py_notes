[1, 1, 5, 6, 9, 16, 27], n=4  -->  3  # (1,5), (1,5), (5,9)
[1, 1, 3, 3], n=2             -->  4  # (1,3), (1,3), (1,3), (1,3)
Test.assert_equals(int_diff([1, 1, 5, 6, 9, 16, 27], 4), 3)
Test.assert_equals(int_diff([1, 1, 3, 3], 2), 4)


def int_diff(arr, n):
    num=0
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if abs(arr[i]-arr[j])==n:
                num+=1
    return num
    
    
 def int_diff(arr, n):
    return sum(sum(abs(a - b) == n for b in arr[i:]) for i, a in enumerate(arr, 1))
