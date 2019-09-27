import numpy
from random import randint


matrix = numpy.zeros(shape = (4, 4))

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        matrix[i][j] = randint(0, 100)

print(matrix)
soma = 0

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if i == 0:
            if j >= 0:
                pass
        elif i > 0:
            if j >= i:
                pass
            else:
                soma += matrix[i][j]

print(soma)
