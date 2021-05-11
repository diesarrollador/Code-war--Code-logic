""" Cree un programa que filtre una lista de cadenas
y devuelva una lista con solo el nombre de sus amigos.
Si un nombre tiene exactamente 4 letras, ¡puede estar
seguro de que tiene que ser un amigo suyo! De lo contrario,
puede estar seguro de que no ... """
def friend(x):
    y=[]
    for i in x:
        y.append(i) if len(i) == 4 else False
    return y
    
print(friend(["Jimm", "Cari", "aret", "truehdnviegkwgvke", "sixtyiscooooool"]))
