from random import randint

vetor1 = list()
vetor2 = list()
vetor3 = list()

for i in range(10):
    vetor1.append(randint(0, 100))
    vetor2.append(randint(0, 100))

for i, e in enumerate(vetor1):
    if i % 2 == 0:
        vetor3.append(vetor1[i])
    else:
        vetor3.append(vetor2[i])

print(f"1: \n {vetor1} \n 2 \n {vetor2} \n")

for i, e in enumerate(vetor3):
    print(i, e)