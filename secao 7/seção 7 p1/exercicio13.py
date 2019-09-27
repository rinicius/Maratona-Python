def lervaloresinteiros():
    vetor1 = input('Insira os numeros abaixo\n')
    vetor1 = vetor1.split()
    vetor1 = [int(i) for i in vetor1]
    return vetor1


vetor1 = lervaloresinteiros()

posmin = 0
posmax = 0

for i in vetor1:
    if i == min(vetor1):
        posmin = vetor1.index(i)
    elif i == max(vetor1):
        posmax = vetor1.index(i)
    else:
        pass

print(f'posição do maior valor: {posmax}')
print(f'posição do menor valor: {posmin}')
