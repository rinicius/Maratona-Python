from random import randint

vetor1 = list()
vetor2 = list()

for i in range(10):
    vetor1.append(randint(150, 200))
    print(vetor1[i])

maximo = max(vetor1)
minimo = min(vetor1)


imaximo = vetor1.index(maximo)
iminimo = vetor1.index(minimo)


print(f"O aluno {imaximo} tem a maior altura com {maximo} \nO aluno {iminimo} tem a menor altura com {minimo}")
