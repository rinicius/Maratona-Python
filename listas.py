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

# Possivel adicionar listas dentro da lista

lista.append([1, 2])
print(lista)

# Extend faz o mesmo porem com mais valores

lista.extend([1, 3, 4, 5, 6, 7, 11, 33, 4])
print(lista)

lista.extend("eae")
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
