""" En este desafío, el usuario ingresa una
cadena y una subcadena. Debe imprimir el
número de veces que ocurre la subcadena 
en la cadena dada. El recorrido de la
cadena se realizará de izquierda a derecha,
no de derecha a izquierda. """
count_substring = lambda s, sb: len([j for j in [1 if s[i : len(sb) + i] == sb else 2 for i in range(len(s))] if j == 1])

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)

# Test input:
# ABCDCDC
# CDC
# Output
# 2