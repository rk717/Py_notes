list sort() function will modify the list it is called on.

the sorted() function will create a new list containing a sorted version of the list it is given.
the sorted() function will not modify the list passed as a parameter.
if you want to sort a list but still have the original unsorted version, then you would use the sorted() function.

vegetables = ['squash', 'pea', 'carrot', 'potato']

new_list = sorted(vegetables)

# new_list = ['carrot', 'pea', 'potato', 'squash']
print(new_list)

# vegetables = ['squash', 'pea', 'carrot', 'potato']
print(vegetables)

vegetables.sort()

# vegetables = ['carrot', 'pea', 'potato', 'squash']
print(vegetables)
