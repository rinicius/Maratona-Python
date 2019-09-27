
def lervaloresinteiros():
    vetor1 = input('Insira os numeros abaixo\n')
    vetor1 = vetor1.split()
    vetor1 = [int(i) for i in vetor1]
    return vetor1


vetor1 = lervaloresinteiros()

for i in vetor1:
    if i == max(vetor1):
        print(f'Maior valor: {i}')
    elif i == min(vetor1):
        print(f'Menor valor: {i}')
    else:
        print(i)

media = sum(vetor1) / len(vetor1)

print(f'\nA média é: {media}')