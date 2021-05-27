""" Para una lista dada [x1, x2, x3, ..., xn]
calcule el último dígito (decimal) de 
x1 ^ (x2 ^ (x3 ^ (... ^ xn))). """
def last_digit(lst):
    if lst:
        re=1
        for numero in lst[::-1]:
            re=numero**(re if re<4 else re%4+4)
        return re%10
    else:
        return 1

print(last_digit([2, 2, 2, 0]))
print(last_digit([3, 4, 2]))
print(last_digit([0,0]))
print(last_digit([0,0,0]))
print(last_digit([]))
print(last_digit([12, 30, 21]))
print(last_digit([499942, 898102, 846073]))
print(last_digit([9,9,9]))