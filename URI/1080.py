valores = list()
for i in range(100):
    valores.append(int(input()))

print(max(valores))
print(valores.index(max(valores)) + 1)