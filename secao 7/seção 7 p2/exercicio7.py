import numpy

matrix = numpy.zeros(shape = (10, 10))

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if i < j:
            matrix[i][j] = 2 * i + 7 * j - 2
        elif i == j:
            matrix[i][j] = 3*(i*i) - 1
        else:
            matrix[i][j] = 4 * (i*i*i) - 5 * (j*j) + 1

print(matrix)