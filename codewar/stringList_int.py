Conver string to a list. 

# Python code to convert string to list 

def Convert(string): 
	li = list(string.split(" ")) 
	return li 

# Driver code	 
str1 = "Geeks for Geeks"
print(Convert(str1)) 

# Python code to convert string to list 
def Convert(string): 
	li = list(string.split("-")) 
	return li 

# Driver code	 
str1 = "Geeks-for-Geeks"
print(Convert(str1)) 





---------------------------------------
results = ['1', '2', '3']
>>>results = list(map(int, results))


>>> results = ["1", "2", "3"]
>>> results = [int(i) for i in results]
>>> results
[1, 2, 3]
results = [int(i) for i in results]
