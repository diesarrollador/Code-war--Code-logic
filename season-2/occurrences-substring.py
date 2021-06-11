""" En este desafío, el usuario ingresa una
cadena y una subcadena. Debe imprimir el
número de veces que ocurre la subcadena 
en la cadena dada. El recorrido de la
cadena se realizará de izquierda a derecha,
no de derecha a izquierda. """
def count_substring(string, sub_string):
    count, ver = int(), str()
    for i in range(len(string)):
        ver = string[i : len(sub_string) + i]
        if ver == sub_string:
            count += 1
    return count

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