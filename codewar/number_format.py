如何将 1 变成 1.00

return format(num, '.2f')
################################
dig_pow(89, 1) should return 1 since 8¹ + 9² = 89 = 89 * 1
dig_pow(92, 1) should return -1 since there is no k such as 9¹ + 2² equals 92 * k
dig_pow(695, 2) should return 2 since 6² + 9³ + 5⁴= 1390 = 695 * 2
dig_pow(46288, 3) should return 51 since 4³ + 6⁴+ 2⁵ + 8⁶ + 8⁷ = 2360688 = 46288 * 51

def dig_pow(n, p):
    # your code
    n_list = [int(i) for i in str(n)]
    n_sum = 0
    p_i = p
    for n_i in n_list:
        n_sum = n_sum + n_i**p_i
        p_i = p_i+1
    if n_sum%n == 0:
        return n_sum/n
    else:
        return -1
