Conver string to a list. 

# Python code to convert string to list 

def Convert(string): 
	li = list(string.split(" ")) 
	return li 

# Driver code	 
str1 = "Geeks for Geeks"
print(Convert(str1)) 
---------------------------------------------------------------


# Python code to convert string to list 
def Convert(string): 
	li = list(string.split("-")) 
	return li 

# Driver code	 
str1 = "Geeks-for-Geeks"
print(Convert(str1)) 
----------------------------------------------------

# Python3 program to Split string into characters 
def split(word): 
	return [char for char in word] 
	
# Driver code 
word = 'geeks'
print(split(word)) 


#['g', 'e', 'e', 'k', 's']



---------------------------------------
results = ['1', '2', '3']
>>>results = list(map(int, results))


>>> results = ["1", "2", "3"]
>>> results = [int(i) for i in results]
>>> results
[1, 2, 3]
results = [int(i) for i in results]

------------------------------------------
How to print list in python??
# Python program to print list 
# using for loop 
a = [1, 2, 3, 4, 5] 

# printing the list using loop 
for x in range(len(a)): 
	print a[x]
	
----------------------------------------------
# Python program to convert a list 
# of character 

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
# Python program to convert a list 
# of character 

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

