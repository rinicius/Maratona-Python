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
            if j == 0:
                pass
            elif j > 0:
                soma += matrix[i][j]
        else:
            if j >= i+1:
                soma += matrix[i][j]
            else:
                pass

print(soma)




