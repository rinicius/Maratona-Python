import numpy
from random import randint

tam = 0
x = int(input('insira o valor a ser encontrado na matriz'))

matrix = numpy.zeros(shape = (5, 5))

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        matrix[i][j] = randint(0, 30)
        tam += 1

print(matrix)
posicoes = []

cont = 0

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] == x:
            posicoes.append((i+1, j+1))
        else:
            cont += 1

if cont == tam:
    print('o valor nao foi encontrado')
else:
    print(f'o valor foi encontrado nas posicoes: \n')
    for e in range(len(posicoes)):
        print(posicoes[e])


