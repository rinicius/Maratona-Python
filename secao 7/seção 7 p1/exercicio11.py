vetor1 = input('Insira os numeros abaixo\n')
vetor1 = vetor1.split()
vetor1 = [int(i) for i in vetor1]

cont = 0
soma = 0

for i in vetor1:
    if i < 0:
        cont += 1
    else:
        soma += i

print(cont, soma)

