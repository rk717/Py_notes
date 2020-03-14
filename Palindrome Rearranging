def palindrome_rearranging(s):
  return [s.count(i) % 2 for in set(s)].count(1) == len(s)%2
  
THINKINGS: 
if your str is even length,
  all your letters must appear an even number of times.
if your str is odd length, 
  you must have exactly 1 letter appear an odd number of times.

Explaination
Doing in Python REPL

>>> s = "abracadabra"

>>> set(s) 
{'a', 'b', 'c', 'd', 'r'}

>>> s.count('a')
5
# number of 'a' s

>>> s.count('a') % 2 
1
# 1 (if number of 'a' is even); 0 (if number of 'a' is odd)

>>> s.count('r') % 2
0
# 1 (if number of 'r' is even); 0 (if number of 'r' is odd)

>>> [s.count(i) % 2 for i in set(s)] 
[1, 1, 1, 0, 0] 
# get all of the 0/1 (even/odd) indicators
 
>>> [s.count(i) % 2 for i in set(s)] .count(1)
3
# the number of letters which there are an odd number of 3

>>> len(s) % 2 
1
# 1 if the length of s is odd, 0 if even

>>> [s.count(i) % 2 for i in set(s)].count(1) == len(s) % 2 
False
# 1==3 



easy way: 

from collections import Counter

def can_be_rearranged_to_palindrome(s):
  letter_counts = Counter(s)
  number_of_odds = sum (1 for c in letter_counts.values() if c % 2 == 1)
  if len(s) % 2 == 0:
    return number_of_odds == 0
  else:
    return number_of_odds == 1
