import math
# dezena - quantidade

"""Exemplo de Saída 
1 2 10 14 20 45 
0 2 1 2 2 1 4 1 
 
 """

while True:
    lista = list()
    entrada = input()
    if entrada == '0':
        break
    lista = entrada.split()
    lista = [int(i) for i in lista]

    
    msg = ''
    cont = [0, 0, 0, 0, 0, 0, 0]

    for i in range(len(lista)):
        if lista[i] < 10:
            cont[0] += 1
        elif lista[i] == 60:
            cont[6] += 1
        else:
            cont[math.floor(lista[i] / 10)] += 1
    

    for i in range(len(cont)):
        if cont[i] == 0:
            pass
        else:
            msg += f'{i} {cont[i]} '
    
    print(msg)