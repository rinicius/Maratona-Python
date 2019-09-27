from random import randint

vetor1 = list()

for i in range(11):
    vetor1.append(randint(0, 20))
print(vetor1)

vetor2 = vetor1[:6:]
print(f'vetor2 {vetor2}')
vetor2.sort()

vetor3 = vetor1[6::]
vetor3.sort(reverse=True)

print(vetor2, vetor3)

vetor2.extend(vetor3)

vetor1 = vetor2

print(vetor1)



