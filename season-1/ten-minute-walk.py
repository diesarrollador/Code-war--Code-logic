""" Vives en la ciudad de Cartesia, donde todas
las carreteras están trazadas en una cuadrícula 
perfecta. Llegó diez minutos antes de una cita, 
por lo que decidió aprovechar la oportunidad para
dar un pequeño paseo. La ciudad ofrece a sus ciudadanos 
una aplicación de generación de caminatas en sus teléfonos:
cada vez que presiona el botón, le envía una serie de 
cadenas de una letra que representan direcciones para 
caminar (por ejemplo, ['n', 's', 'w', 'mi']). Siempre
caminas solo una cuadra por cada letra (dirección) y 
sabes que te lleva un minuto atravesar una cuadra de la
ciudad, así que crea una función que se vuelva verdadera 
si la caminata que te da la aplicación te llevará exactamente 
diez minutos (tú ¡No quiero llegar temprano o tarde!) y,
por supuesto, lo devolverá a su punto de partida.
Devolver falso en caso contrario. """
def is_valid_walk(walk):
    ns, ew = 0, 0
    if len(walk) == 10:
        for i in walk:
            if i == 'n': ns += 1
            if i == 's': ns -= 1
            if i == 'w': ew += 1
            if i == 'e': ew -= 1
        return True if ns == 0 and ew == 0 else False
    return False

print(is_valid_walk(['n','s','n','s','n','s','n','s','n','w']))