def accum(s):
    ans = ''                                  #initialize ans as an empty string
    i = 0                                     #initialize the counter i to zero
    while i < len(s):                         #begin while loop, iterating while i is less than the length of s, which is a string. 
        n = 0                                 #initialize n to zero
        while n < i+1:                        #iterating while n is less than or equal to i. Here, i is the index of the current character. 
            if n == 0:                        #if n is the first loop iteration. 
                ans += s[i].upper()
            else:
                ans += s[i].lower() 
            n += 1                            #increment n so that the while loop doesn't run forever
        ans += '-'                            #append a hyphen to the answer once the inner while loop is completed
        i += 1                                #increment the counter for the outer while loop
    return ans[:len(ans)-1]                   #selcect the whole ans except for teh last entry
    
   
accum("abcd") -> "A-Bb-Ccc-Dddd"

accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"

accum("cwAt") -> "C-Ww-Aaa-Tttt"



def accum(s):
	ans = ''
	for i, letter in enumerate(s, start=1):
		ans += (letter * i) + '-'
	ans = ans.split('-')[0:-1]
	return '-'.join(ans).title()
