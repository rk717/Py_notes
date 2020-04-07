Test.describe("Basic tests")
Test.assert_equals(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]), "(123) 456-7890")
Test.assert_equals(create_phone_number([1, 1, 1, 1, 1, 1, 1, 1, 1, 1]), "(111) 111-1111")
Test.assert_equals(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]), "(123) 456-7890")
Test.assert_equals(create_phone_number([0, 2, 3, 0, 5, 6, 0, 8, 9, 0]), "(023) 056-0890")
Test.assert_equals(create_phone_number([0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), "(000) 000-0000")


def create_phone_number(n):
    #your code here
    #[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), "(000) 000-0000"

    phone = ''
    for num in n[0:3]:
        phone = phone + str(num)
    set1 = ''
    for num in n[3:6]:
        set1 = set1 + str(num)
    
    set2 = ''
    for num in n[6:]:
        set2 = set2 + str(num)
    res = '('+phone+")"+" "+set1+"-"+set2
    return res
print(create_phone_number([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))


--------------------------------------------------------------------
def create_phone_number(n):
    return "({}{}{}) {}{}{}-{}{}{}{}".format(*n)
    
----------------------------------------------------------------------
def create_phone_number(n):
  str1 =  ''.join(str(x) for x in n[0:3])
  str2 =  ''.join(str(x) for x in n[3:6])
  str3 =  ''.join(str(x) for x in n[6:10])


  return '({}) {}-{}'.format(str1, str2, str3)
  
  -----------------------------------------------------------------------
  def create_phone_number(n):
    n = ''.join(map(str,n))
    return '(%s) %s-%s'%(n[:3], n[3:6], n[6:])
  
