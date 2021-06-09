""" Inicialice su lista y lea el valor de N
seguido de líneas de comandos donde
cada comando será de los tipos:
insert, print, remove, append, sort,
pop y reverse. Repita cada comando en orden
y realice la operación correspondiente en su lista. """
def commands(lista):
    out2 = list()
    for command in lista:
        if 'remove' in command:
            out2.remove(int(command.split()[1]))
        elif 'insert' in command:
            out2.insert(int(command.split()[1]), int(command.split()[2]))
        elif 'append' in command:
            out2.append(int(command.split()[1]))
        elif 'sort' in command:
            out2.sort()
        elif 'pop' in command:
            out2.pop()
        elif 'reverse' in command:
            out2.reverse()
        elif 'print' in command:
            yield out2

if __name__ == '__main__':
    data, lista = str(), list()
    N = int(input())
    for _ in range(N):
        data = input()
        lista.append(data)
    for i in commands(lista):
        print(i)

# Test Input:
# 12
# insert 0 5
# insert 1 10
# insert 0 6
# print
# remove 6
# append 9
# append 1
# sort
# print
# pop
# reverse
# print

# Output
# [6, 5, 10]
# [1, 5, 9, 10]
# [9, 5, 1]