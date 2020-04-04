def square(list):
    return [i ** 2 for i in list]
    
def square(list):
    return map(lambda x: x ** 2, list)
    
def square(list):
    for i in list:
        yield i ** 2
        
def square(list):
    ret = []
    for i in list:
        ret.append(i ** 2)
    return ret
