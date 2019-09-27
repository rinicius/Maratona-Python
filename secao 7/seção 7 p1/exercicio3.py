
print('Insira os números na linha abaixo')
a1 = input()
vetor1 = a1.split()

for i in vetor1:
    index = vetor1.index(i)
    vetor1[index] = float(i)
    print(vetor1[index])
    vetor1[index] = vetor1[index] ** 2
    print(vetor1[index])


