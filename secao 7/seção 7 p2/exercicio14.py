import numpy
from random import randint

cartela = numpy.zeros(shape = (5, 5))
numero = 0

for i in range(len(cartela)):
    for j in range(len(cartela[i])):
        while True:
            numero = randint(0, 99)
            if numero in cartela:
                pass
            else:
                cartela[i][j] = numero
                break;

print(cartela)
        
