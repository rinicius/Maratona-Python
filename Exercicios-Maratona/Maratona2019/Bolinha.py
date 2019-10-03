def resultado (n):
    fatorial = 1
    while n > 0:
        fatorial *= n
        n -= 1
        
    return fatorial


def mensagem (n):
    fatorial = n
    for i in range(len(nprimo)):
        if resultado(nprimo[i]) == n:
            n = nprimo[i]
            np = nprimo[i]
    
    lista = list()
    while n > 0:
        n -= 1
        lista.append(n)

    lista.pop(-1)

    msg = ''
    msg += f'{np}! = '

    for i in range(len(lista)):
        if lista[i] == lista[0]:
            msg += f'{np} . '

        if lista[i] == lista[-1]:
            msg += f'{lista[i]} = {fatorial}'
        else:
           msg += f'{lista[i]} . '
    return msg


nprimo = (2, 3, 5, 7, 11, 13, 17, 19)
resultadoPrimos = [resultado(nprimo[0]), resultado(nprimo[1]), resultado(nprimo[2]), resultado(nprimo[3]), resultado(nprimo[4]), resultado(nprimo[5]), resultado(nprimo[6]), resultado(nprimo[7])]
#2, 3, 5, 7, 11, 13, 17, 19 
while True:
    n1 = int(input())

    if n1 == 0:
        break


    if n1 in resultadoPrimos:
        print(mensagem(n1)) 
