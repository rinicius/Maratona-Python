vetor1 = list(range(51))
i = 0
print(vetor1)

while i < 51:
    vetor1[i] = (i+5*i) % (i+1)
    i += 1

print(vetor1)
