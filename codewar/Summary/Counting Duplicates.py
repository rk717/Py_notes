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

-------------------------------------------------------
把 单词 放到 字典里 数字母

def string_letter_count(s):
    counts = {}
    for char in s.lower():
        counts[char] = counts.get(char, 0) + 1
    return counts

print(string_letter_count("hello"))

#{'h': 1, 'e': 1, 'l': 2, 'o': 1}

------------------------------------------------------
去除一个 数组/字符串 的 多余字符
unique_in_order('AAAABBBCCDAABBB') == ['A', 'B', 'C', 'D', 'A', 'B']
unique_in_order('ABBCcAD')         == ['A', 'B', 'C', 'c', 'A', 'D']
unique_in_order([1,2,2,3,3])       == [1,2,3]

def unique_in_order(iterable):
    result = []
    prev = None
    for char in iterable[0:]:
        if char != prev:
            result.append(char)
            prev = char
    return result

---------------------------------------
def unique_in_order(iterable):
    newList = []
    for item in iterable:
        if len(newList) < 1 or not item == newList[len(newList) - 1]:
            newList.append(item)
    return newList
