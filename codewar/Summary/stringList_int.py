判断是不是密码
validate_pin("1234") == True
validate_pin("12345") == False
validate_pin("a234") == False

def validate_pin(pin):
    return len(pin) in (4, 6) and pin.isdigit()

validate_pin = lambda pin: len(pin) in [4,6] and pin.isdigit()
--------------------------------------
把一串字符串转换成 ‘#’ ， 只保留最后 4 位
def maskify(cc):
    return "#"*(len(cc)-4) + cc[-4:]
maskify(     "64607935616") ==      "#######5616"


------------------------------------
字符串去除重复
mylist = ["a", "b", "a", "c", "c"]
mylist = list(dict.fromkeys(mylist))
#["a", "b", "c"]

def longest(a1, a2):
    return "".join(sorted(set(a1 + a2)))

def longest(s1, s2):
    return ''.join(sorted(set(s1).union(s2)))

--------------------------------------
删除 字符串里的大写字母
def duplicate_encode(word):
    #your code here
    s = ''.join(ch for ch in word if not ch.isupper())
    return s

print(duplicate_encode("Hello"))
#ello

---------------------------------
replace字符
def DNAtoRNA(dna):
    return (dna.replace("T", "U"))

replace 一个字符串的数组
def song_decoder(song):
    song = song.split('WUB')
    original_song = []
    for i in song:
        if i != '':
            original_song += [i]
    return ' '.join(original_song)

print(song_decoder("AWUBBWUBC"))
#A B C

-----------------------------------
反转一句话：
def reverseWords(s):
    return " ".join(s.split()[::-1])
---------------------------------
反转字符串
reverse a string:

def solution(str):
	return str[::-1]

str = 'Python' 
reversed=''.join(reversed(str)) 
# .join() method merges all of the characters resulting from the reversed iteration into a new string


----------------------------------
反转列表
reverse a list:
def Reverse(lst): 
	lst.reverse() 								
	return lst 

lst = [10, 11, 12, 13, 14, 15] 
print(Reverse(lst)) 

------------------------------------
转换字符串到列表
Conver string to a list. 

def Convert(string): 
	li = list(string.split(" ")) 
	return li 

str1 = "Geeks for Geeks"
print(Convert(str1))

#['Geeks', 'for', 'Geeks']
---------------------------------------------------------------
def Convert(string): 
	li = list(string.split("-")) 
	return li 


str1 = "Geeks-for-Geeks"
print(Convert(str1)) 
#['Geeks', 'for', 'Geeks']
----------------------------------------------------

字符串变单个字符
def split(word): 
	return [char for char in word]         # list(world)
	
# Driver code 
word = 'geeks'
print(split(word)) 


#['g', 'e', 'e', 'k', 's']



---------------------------------------
把列表里的 字符串 变成 int
results = ['1', '2', '3']
>>>results = list(map(int, results))


>>> results = ["1", "2", "3"]
>>> results = [int(i) for i in results]
>>> results
[1, 2, 3]
results = [int(i) for i in results]

------------------------------------------
如何打印list

a = [1, 2, 3, 4, 5] 

# printing the list using loop 
for x in range(len(a)): 
	print a[x]
	
----------------------------------------------
把字符变成list

def convert(s): 

	# initialization of string to "" 
	new = "" 

	# traverse in the string 
	for x in s: 
		new += x 

	# return string 
	return new 
	
	
# driver code 
s = ['g', 'e', 'e', 'k', 's', 'f', 'o', 'r', 'g', 'e', 'e', 'k', 's'] 
print(convert(s)) 

#geeksforgeeks

----------------------------------------------------------------------------
把字符变成list
def convert(s): 

	# initialization of string to "" 
	str1 = "" 

	# using join function join the list s by 
	# separating words by str1 
	return(str1.join(s)) 
	
# driver code 
s = ['g', 'e', 'e', 'k', 's', 'f', 'o', 'r', 'g', 'e', 'e', 'k', 's'] 
print(convert(s)) 

#geeksforgeeks

---------------------------------------------------------------------------------
把列表里的字符串变成字符串 
test.assert_equals(smash(["hello"]), "hello")
test.assert_equals(smash(["hello", "world"]), "hello world")

def smash(words):
    return " ".join(words)
---------------------------------------------------------------------------------
一串列表里只pick数字
[s for s in myList if s.isdigit()]


-----------------------------------------
list_1 = [ 'asdada', 1, 123131.131, 'blaa adaraerada', 0.000001, 34.12451235265, 'stackoverflow is awesome' ]
import operator
filter(operator.isNumberType, list_1

       
       
       
------------------------------------------------------------------
查询一个stirng里有多少个特定的 char
strCount('Hello', 'o') // => 1
strCount('Hello', 'l') // => 2
strCount('', 'z')      // => 0
       
def strCount(string, letter):
    return string.count(letter)
       
------------------------------------------------------------------
查询一个list里有没有一个特定的element

       def check(seq, elem):
    for i in seq:
        if i == elem:
            return True
    return False

print(check([101, 45, 75, 105, 99, 107], 107))

       
def check(seq, elem):
    return elem in seq
       
--------------------------------------------------------------------
将数字字符串转化成 integer

test_list = ['1', '4', '3', '6', '7'] 
for i in range(0, len(test_list)): 
	test_list[i] = int(test_list[i]) 
       
----------------------------------------------------
test_list = [int(i) for i in test_list] 
       
-----------------------------------------------------
test_list = list(map(int, test_list)) 
       
---------------------------------------------------------------------
数出字符串里面有几个 “1”
       
def countBits(n):
    return bin(n).count("1")
       
------------------------------------------------------------------
让一个数组里的数全部各自相乘
def multiplyList(myList) : 
    result = 1
    for x in myList: 
         result = result * x  
    return result  
       
----------------------------------------------------------------------
把一串字符串 转化 成 “（” 和 “）”， 如果字母出现一次，用‘（’， 出现多次 用 ‘）’ ， 大写字母不参与 count
def duplicate_encode(word):
    """a new string where each character in the new string is '(' 
    if that character appears only once in the original word, or ')' 
    if that character appears more than once in the original word. 
    Ignores capitalization when determining if a character is a duplicate. """
    word = word.upper()
    result = ""
    for char in word:
        if word.count(char) > 1:
            result += ")"
        else:
            result += "("
            
    return result
-----------------------------------
def duplicate_encode(word):
	return "".join(["("if word.lower().count(c) == 1 else ")" for c in word.lower() ] )
       
Test.assert_equals(duplicate_encode("din"),"(((")
Test.assert_equals(duplicate_encode("recede"),"()()()")
Test.assert_equals(duplicate_encode("Success"),")())())","should ignore case")
Test.assert_equals(duplicate_encode("(( @"),"))((")
