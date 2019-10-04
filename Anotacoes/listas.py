import numpy
from random import randint
""""listas em python = array
são dinâmicos
QUALQUER tipo de dado
"""

lista = [1, 2, 3, 5, 6, 3, 2, 2]

cont = 2

if cont in lista:
    print('Achei o numero ' + str(cont))
    print(f'Achei o numero {cont}')

# Organiza a lista

lista.sort()
print(lista)

# Conta quantos elementos tem na lista

contagem = lista.count(2)
print(contagem)

# Adiciona 1 valor na lista

lista.append(1)
print(lista)

# Extend faz o mesmo porem com mais valores

lista.extend([1, 3, 4, 5, 6, 7, 11, 33, 4])
print(lista)

lista.extend("eae")
print(lista)

# Possivel adicionar listas dentro da lista

lista.append([1, 2])
print(lista)


# Possivel escolher o indice para adicionar

posicao = 2
elemento = 'oi'
lista.insert(posicao, elemento)
print(lista)

# Possivel somar duas listas
"""
lista = lista + lista
print(lista)
"""

lista2 = lista.copy()
print(f'aqui {lista2}')

# Remove e retorna o ultimo elemento

print(lista.pop())

# Remove e retorna algum elemento na posição desejada

print(lista.pop(2))

# Remove todos os elementos

print(lista.clear())
lista = [1, 3, 4, 5]

# Da pra somar a lista com multiplicação

print(f'Lista normal {lista}')
print(f'lista multiplicada {lista * 3}')

# Split:

lista = 'Vinicius Rocha da Silva'
lista = lista.split()
print(lista)

lista = 'Vinicius,Rocha,da,Silva'
lista = lista.split(',')
print(lista)

# Split para string dnv

lista = ' '.join(lista)
print(lista)

lista = lista.split()

# Enumerar um array

for indice, elemento in enumerate(lista):
    print(enumerate(lista))
    print(indice, elemento)
    print('enumerado')

"""esse tmb è foda"""

lista = list(enumerate(lista))
print(type(lista[0]))

# Encontrar um índice de algum elemento

listanova = list(range(1, 3000))

print(listanova.index(43))
# E caso tenha algum numero repetido, cria um range com um indice de qual começar a buscar
listanova.append(43)

print(listanova.index(43, 43))

# SLICING:
# (inicio:fim:passo)

listanova1 = list(range(11))

print(listanova1[1:])  # Começa do 1 e vai pra todo resto
print(listanova1[::])  # Todos os elementos
print(listanova1[::2])  # Começa do 0, vai ate o final e passa de 1 em 1
# OBS...
print(listanova1[::-1])  # Inverte as posições da lista

# Basisco

print(sum(listanova1), min(listanova1), max(listanova1))

# Descompactamento de lista

listastring = 'Vinicius rocha da silva'.split()

pnome, snome, tnome, qnome = listastring
print(pnome, snome)

# Copia de listas

listanovacopia = listanova1.copy()
listanovacopia.append(3)

print(listanovacopia)
print(listanova1)

# Uma lista não afeta outra
# = Deep copy

listanovacopia = listanova1
listanovacopia.append(3)

print(listanovacopia)
print(listanova1)

# Aqui, as duas listas agora dependem uma da outra
# caso uma mude, a outra muda também
# = shallow copy


lista11 = ['a', 'b', 'a']

print(lista11.count('a'))

# Matrix

m = 4  # Numero de linhas
a = [[0] * m, [0] * m]  # Multiplica o tanto de colunas que vai ter o tanto de linhas q vai ter

print(a)
print('\n')

# Criando uma matrix com valores aleatórios com numpy

matrix = numpy.random.randint(low = 0, high = 10, size = (2, 4)) # Low = menor valor \\ high = maior valor \\ size =
# tamanho da matrix
print(matrix)
