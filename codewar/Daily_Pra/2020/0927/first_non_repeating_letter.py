def first_non_repeating_letter(string):
    list = [i.lower() for i in string]
    for i in range(len(list)):
        if list.count(list[i]) == 1:
            return string[i]
    return ''

#https://www.codewars.com/kata/52bc74d4ac05d0945d00054e/python