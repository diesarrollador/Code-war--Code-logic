""" Se le da una clase de jugo, que tiene propiedades de
nombre y capacidad. Debe completar el código para
habilitar y agregar dos objetos Juice, lo que da
como resultado un nuevo objeto Juice con la capacidad 
combinada y los nombres de los dos jugos que se agregan.
Por ejemplo, si agrega un jugo de naranja con una 
capacidad de 1.0 y un jugo de manzana con una capacidad 
de 2.5, el jugo resultante debe tener: 
nombre: capacidad de naranja y manzana: 3.5 
Los nombres se han combinado usando un símbolo &. """
class Juice:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity

    def __str__(self):
        return (self.name + ' ('+str(self.capacity)+'L)')

    def __add__(self, otro):
        return '{}&{} ({}L)'.format(self.name, otro.name, self.capacity + otro.capacity)


a = Juice('Orange', 1.5)
b = Juice('Apple', 2.0)

result = a + b
print(result)