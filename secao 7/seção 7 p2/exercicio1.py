from random import randint
import numpy as np


matrix = np.zeros(shape = (4, 4))

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        matrix[i][j] = randint(0, 30)


cont = 0

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] > 10:
            cont += 1
        else:
            pass

print(matrix)

print(f'Há {cont} numeros 10 na matrix')
