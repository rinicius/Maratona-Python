vetor1 = list()
cont = 0
mult = 0

while cont < 10:
    vetor1.append(0.5 + mult)
    mult += 0.5
    cont += 1

cont = 0
vetor2 = list()

for i in range(len(vetor1)):
    if vetor1[i] % 2 == 0:
        pass
    else:
        vetor2.append(vetor1[i])

print(f"{vetor1} \n {vetor2}")

