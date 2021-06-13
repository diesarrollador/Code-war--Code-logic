""" Dado un número entero, n, imprime los 
siguientes valores para cada entero i 1 a n
1. Decimal
2. Octal
3. Hexadecimal (capitalized)
4. Binario
Los cuatro valores deben imprimirse en una sola
línea en el orden especificado anteriormente 
para cada i de 1 a number. Cada valor debe rellenarse 
con un espacio para que coincida con el ancho del valor
binario de number y los valores deben estar separados 
por un solo espacio.
"""
def print_formatted(number):
    for i in range(1, number + 1):
        print(str(i).rjust(len(bin(number)[2:]), " "), oct(i)[2:].rjust(len(bin(number)[2:]), " "), hex(i).upper()[2:].rjust(len(bin(number)[2:]), " "), bin(i)[2:].rjust(len(bin(number)[2:]), " "))
        
if __name__ == '__main__':
    n = int(input())
    print_formatted(n)

# Test input: 
# 17

# Output
#    1     1     1     1
#    2     2     2    10
#    3     3     3    11
#    4     4     4   100
#    5     5     5   101
#    6     6     6   110
#    7     7     7   111
#    8    10     8  1000
#    9    11     9  1001
#   10    12     A  1010
#   11    13     B  1011
#   12    14     C  1100
#   13    15     D  1101
#   14    16     E  1110
#   15    17     F  1111
#   16    20    10 10000
#   17    21    11 10001