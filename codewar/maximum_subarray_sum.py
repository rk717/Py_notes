test.describe("Tests")
test.it('should work on an empty array')   
test.assert_equals(max_sequence([]), 0)
test.it('should work on the example')
test.assert_equals(max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4]), 6)

The maximum sum subarray problem consists in finding the maximum sum of a contiguous subsequence in an array or list of integers:

maxSequence([-2, 1, -3, 4, -1, 2, 1, -5, 4])
# should be 6: [4, -1, 2, 1]

-----------------------------------------------------------


def max_sequence(a): 
	size = len(a)
	max_so_far = 0
	max_ending_here = 0
	
	for i in range(0, size): 
		max_ending_here = max_ending_here + a[i] 
		if max_ending_here < 0: 
			max_ending_here = 0
		
		# Do not compare for all elements. Compare only 
		# when max_ending_here > 0 
		elif (max_so_far < max_ending_here): 
			max_so_far = max_ending_here 
			
	return max_so_far 


----------------------------------------------------------------
def maxSequence(arr):
    lowest = ans = total = 0
    for i in arr:
        total += i
        lowest = min(lowest, total)
        ans = max(ans, total - lowest)
    return ans
-------------------------------------------------------------------
def maxSequence(arr):
    max,curr=0,0
    for x in arr:
        curr+=x
        if curr<0:curr=0
        if curr>max:max=curr
    return max
