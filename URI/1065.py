cont = 0
for i in range(5):
    intei = int(input())
    if intei%2 == 0:
        cont += 1
print('{} valores pares'.format(cont))