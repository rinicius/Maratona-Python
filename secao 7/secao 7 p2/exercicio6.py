import numpy
from random import randint

matrix1 = numpy.zeros(shape = (4, 4))
matrix2 = numpy.zeros(shape = (4, 4))
matrix3 = numpy.zeros(shape = (4, 4))

for i in range(len(matrix1)):
    for j in range(len(matrix1[i])):
        matrix1[i][j] = randint(0, 30)
        matrix2[i][j] = randint(0, 30)

for i in range(len(matrix1)):
    for j in range(len(matrix1[i])):
        if matrix1[i][j] > matrix2[i][j]:
            matrix3[i][j] = matrix1[i][j]
        else:
            matrix3[i][j] = matrix2[i][j]

print(f'{matrix1}\n')
print(f'{matrix2}\n')
print(f'Maiores valores: \n{matrix3}')

