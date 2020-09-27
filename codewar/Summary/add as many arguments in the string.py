Test.assert_equals(build_string('Cheese','Milk','Chocolate'), 'I like Cheese, Milk, Chocolate!', 'Return the correct String')

Test.assert_equals(build_string('Cheese','Milk'), 'I like Cheese, Milk!', 'Return the correct String')

Test.assert_equals(build_string('Chocolate'), 'I like Chocolate!', 'Return the correct String')

def build_string(*args):
    return "I like {}!".format(", ".join(args))
    
def build_string(*args):
    lst = []
    for i in args:
        lst.append(i)
    return "I like " + ", ".join(lst) + "!"
