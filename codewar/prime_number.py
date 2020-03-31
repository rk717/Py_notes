import math
def is_prime(n):
    if n % 2 == 0 and n > 2:
        return False
    for i in range(3, int(math.sqrt(n)) + 1 , 2):           # math.sqrt(n) 后面 + 1 是因为python range 不包括最后一个数
        if n % i == 0:
            return False
    return True

print(is_prime(99))
