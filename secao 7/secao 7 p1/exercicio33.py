from random import randint

vetor1 = list()

for i in range(15):
    vetor1.append(randint(0, 10))

print(vetor1)

for i in vetor1:
    if i == 0:
        vetor1.pop(vetor1.index(i))

print(vetor1)