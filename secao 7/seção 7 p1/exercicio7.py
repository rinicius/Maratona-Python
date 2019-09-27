vetor1 = input('Insira os numeros abaixo\n')
vetor1 = vetor1.split()

print(vetor1)
menor = min(vetor1)
menori = vetor1.index(menor)

maior = max(vetor1)
maiori = vetor1.index(maior)

print(f'O maior valor é {maior} na posição {maiori+1}')
print(f'O menor valor é {menor} na posição {menori+1}')