""" La persona X es dueña de una zapatería.
Su tienda tiene X número de zapatos.
Tiene una lista que contiene la talla de
cada zapato que tiene en su tienda.
Hay N número de clientes que están dispuestos 
a pagar x cantidad de dinero solo si obtienen
el zapato de la talla deseada.
Su tarea es calcular cuánto dinero ganó esa persona. 

Formato de entrada:
1. La primera línea contiene X, el número de zapatos.
2. La segunda línea contiene la lista separada por espacios
de todas las tallas de zapatos en la tienda.
3. La tercera línea contiene N, el número de clientes.
4. Las siguientes N líneas contienen los valores separados por
espacios de la talla de zapato deseada por el 
cliente y x, el precio del zapato.
"""
from collections import Counter
def shoe_shop(tallas: list, lista_clientes: list) -> int:
    out = list()
    tallas_dic = Counter(tallas)
    for clie in lista_clientes:
        if clie[0] in tallas_dic.keys():
            if tallas_dic.get(clie[0]) > 0:
                out.append(clie[-1])
                tallas_dic[clie[0]] -= 1
    return sum(out)
            
if __name__ == "__main__":
    lista_clientes = list()
    x = int(input())
    tallas = list(map(int, input().split()))
    clientes = int(input())
    for _ in range(clientes):
        datos = list(map(int, input().split()))
        lista_clientes.append(datos)
    print(shoe_shop(tallas, lista_clientes))

# Test input:
# 10
# 2 3 4 5 6 8 7 6 5 18
# 6
# 6 55
# 6 45
# 6 55
# 4 40
# 18 60
# 10 50

#Output
# 200