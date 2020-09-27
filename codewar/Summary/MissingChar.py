["a","b","c","d","f"] -> "e"
["O","Q","R","S"] -> "P"

def find_missing_letter(chars):
    missingChar = ""
    for i in range(0, len(chars)-1):
        if(ord(chars[i+1]) - ord(chars[i]) > 1):
            missingChar = chr(ord(chars[i]) + 1)
    
    return missingChar

