"""
1
10
Pen1 N
JPen J
Pen2 N
Pc V
Pc2 N
Monitor A
Celular F
Pen V
abc N
teste A
"""

vzs = int(input())
qtd = int(input())

while vzs > 0:
    lista2 = list(range(qtd))
    lista = list()
    cat = list()
    for i in range(qtd):
        entrada = input()
        lista.append(entrada)
        cat.append(entrada.split()[1])
    
    msg = ''
    cont = 0
    contv = 0
    conta = 0
    contf = 0

    for i in range(len(lista)):
        if cat[i] == 'F':
            lista2.insert(i-3 if i != 0 else 0 + contf, lista[i])
            #lista2[i-3 if i != 0 else 0 + contf] = lista[i]
            contf += 1
        elif cat[i] == 'A':
           lista2.insert(i-2 if i != 0 else 0 + conta, lista[i])
           #lista2[i-2 if i != 0 else 0 + conta] = lista[i]
           conta += 1
        elif cat[i] == 'V':
            lista2.insert(0 + contv, lista[i])
            #lista2[0 + contv] = lista[i]
            contv += 1
        elif cat[i] == 'J':
            lista2.append(lista[i])

        elif cat[i] == 'N':
            lista2.insert(lista.index(lista[i]), lista[i])



    for i in range(len(lista2)):
        if lista2[i] in range(100):
            pass
        else:
            print(lista2[i])

    vzs -= 1