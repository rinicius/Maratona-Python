import numpy
from random import randint

matrix = numpy.zeros(shape = (3, 3))
matrix1 = numpy.zeros(shape = (3, 3))
matrix2 = numpy.zeros(shape = (3, 3))

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        matrix[i][j] = randint(0, 100)

print(matrix)
aux = []

for j in range(len(matrix[0])):
    linha = []
    for i in range(len(matrix)):
        linha.append(matrix[i][j])
        aux.append(linha)

print(aux)
