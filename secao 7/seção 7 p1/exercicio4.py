vetor1 = input('Digite os valores na linha abaixo\n')
vetor1 = vetor1.split()

pos = input('Insira o valor das posicoes abaixo\n')
pos = pos.split()

soma = int(vetor1[int(pos[0])]) + int(vetor1[int(pos[1])])

print(f'A soma é: {soma}')

