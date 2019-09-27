import random

import numpy



matriz = numpy.zeros(shape = (4, 4))


for i in range(len(matriz)):

    for j in range(len(matriz[i])):

        matriz[i][j] = i+j*3



print(matriz)



for i in range(len(matriz)):

    for j in range(len(matriz[i])):

        if i == 0:

            if j == 0:

                pass

            else:

                matriz[i][j] = 0
        else:

            if j >= i+1:

                matriz[i][j] = 0



print(matriz)

