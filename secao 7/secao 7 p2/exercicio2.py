import numpy
matrix = numpy.zeros(shape = (10, 10))


for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if i == 0:
            if j == 0:
                matrix[i][j] = 1
            else:
                pass
        else:
            if matrix[i-1][j] == 0 and matrix[i-1][j-1] == 1:
                matrix[i][j] = 1
            else:
                pass

print(matrix)
