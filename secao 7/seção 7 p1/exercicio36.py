from random import randint

vetor1 = list()

for i in range(10):
    vetor1.append(randint(0, 100))

vetor1.sort()
print(vetor1)