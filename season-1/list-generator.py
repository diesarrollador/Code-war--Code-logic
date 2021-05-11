listfruit = []
def generar():
    totalList = int(input('Cuántas ensaladas quiere crear: '))
    for i in range(totalList):
        lenlist = int(input(f'Cuántas frutas 🍎 va a incluir en la ensalada {i+1}: '))
        for j in range(lenlist):
            listfruit.append(str(input(f'Nombre de la fruta {j+1}: ')))
        print(f'La ensalada {i+1} tiene {listfruit} \n')
        listfruit.clear()
generar()