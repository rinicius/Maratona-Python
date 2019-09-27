import numpy

matrix = numpy.zeros(shape = (4, 4))

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        matrix[i][j] = i*j

print(matrix)

