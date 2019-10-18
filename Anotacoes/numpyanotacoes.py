import numpy

#array normal para numpy
arr = numpy.arange(0, 10, 2)
print(arr)
print('\n')
print(numpy.array([1, 2, 3, 4, 5]))
print('\n')

#array com matriz
print(numpy.array([[1, 2, 3], [1, 2, 3]]))
print('\n')

#matrizes
print(numpy.zeros((4, 4)))
print('\n')
print(numpy.ones((4, 4)))
print('\n')
print(numpy.eye(4))
print('\n')

#random...
print(numpy.random.rand(5)) #aqui ele cria um array de 1 dimensao com X numeros aleatorios entre 0 e 1
print('\n')
print(numpy.random.rand(5) * 100) #aqui ele cria um array de 1 dimensao com X numeros aleatorios entre 0 e 100
print('\n')
print(numpy.random.rand(2, 2)) #aqui ele cria um array de 2 dimensoes com X colunas e Y linhas com numeros aleatorios entre 0 e 1
print('\n')
#aqui é a distribuicao gaussiana
print(numpy.random.randn(5)) #aqui ele cria um array de 1 dimensao com X numeros aleatorios entre 0 e 1
print('\n')
print(numpy.random.randn(5) * 100) #aqui ele cria um array de 1 dimensao com X numeros aleatorios entre 0 e 100
print('\n')
print(numpy.random.randn(2, 2)) #aqui ele cria um array de 2 dimensoes com X colunas e Y linhas com numeros aleatorios entre 0 e 1
#aqui é random mas com inteiros...
print('\n')
print(numpy.random.randint(0, 100, (2, 2))) 
