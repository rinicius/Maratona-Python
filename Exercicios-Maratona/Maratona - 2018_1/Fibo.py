def fibo(n1):
    resultado = [0, 1, 1]
    cont = 2
    while True:
        total = resultado[cont] + resultado[cont-1]
        resultado.append(total)
        if total == n1:
            break
        cont += 1
        

    return len(resultado)

numeros = list()
while True:
    entrada = int(input())
    if entrada == 0:
        break
    else:
        print(fibo(entrada))