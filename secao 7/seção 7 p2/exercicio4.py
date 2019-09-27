from random import randint
import numpy

matrix = numpy.zeros(shape=(4, 4))

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        matrix[i][j] = randint(0, 100)

resultado = {'maior': 0}

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] == numpy.amax(matrix):
            resultado['maior'] = matrix[i][j]
            resultado['linha'] = i
            resultado['coluna'] = j

print(f'O maior resultado é {resultado["maior"]} e sua posicao é linha {resultado["linha"]}, coluna {resultado["coluna"]}')

