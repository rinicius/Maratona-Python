"""
8 
Alberto 250 
Marco 3 
Suzano 32 
De Lima 54 
Juan 1 
De Souza 24 
Antonio 125 
Polido 100 
0
"""

qtd = int(input())
nomes = list()
numeros = list()

while True:
    entrada = input()
    if entrada == '0':
        break
    else:
        entrada = entrada.split()
        if len(entrada) > 2:
            nomes.append('{} {}'.format(entrada[0], entrada[1]))
            numeros.append(int(entrada[2]))
        else:
            nomes.append(entrada[0])
            numeros.append(int(entrada[1]))


listanu, listano = list(zip(*sorted(zip(numeros, nomes))))

for i in range(len(listano)):
    print('{:03d} {}'.format(listanu[i], listano[i]))


