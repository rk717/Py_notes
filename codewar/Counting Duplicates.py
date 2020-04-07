def max_repeat(word):
    counts = {}  # associate letters with letter count
    max_count = 0  # how many times we've seen a character occur more than once.
    for char in word.lower():  # convert string to lower case
        counts[char] = counts.get(char, 0) + 1  # keep count of the letter counts
    for count in counts.values():  # for each character count in our dictionary
        if count > 1:  # Found a character occuring more than once?
            max_count += 1  # increase our max_count variable
    # max_count = sum(1 for c in counts.values() if c > 1)  # for every letter, if the count exceeds one, let's increment a counter
    return max_count  # return that counter

tests = (
    ("abcde", 0),
    ("aabbcde", 2),
    ("aabBcde", 2),
    ("indivisibility", 1),
    ("Indivisibilities", 2),
    ("aA11", 2),
    ("ABBA", 2),
)

for test, expected in tests:
    print(f'Testing: "{test}"; Expected: {expected}; Received: {max_repeat(test)}')
    
    
---------------------------------------------------------------------------------------
检查一串字符串里是否有重复字母
is_isogram("Dermatoglyphics" ) == true
is_isogram("aba" ) == false
is_isogram("moOse" ) == false # -- ignore letter case




def is_isogram(string):
    return len(string) == len(set(string.lower()))

---------------------------------------------------
def is_isogram(string):
    string = string.lower()
    for letter in string:
        if string.count(letter) > 1: return False
    return True
-----------------------------------------------------
def is_isogram(string):
    #your code here
    word = [char for char in string]
    word = [x.lower() for x in string]
    cnt = 0
    for i in range(len(word)):
        for j in word[i+1:]:
            if word[i] == j:
                cnt += 1
    if cnt > 0:
        return False
    else:
        return True

print(is_isogram("aba"))
