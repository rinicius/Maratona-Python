media = cont = 0
while True:
    idade = int(input())
    if idade < 0:
        break
    else:
        media += idade
        cont += 1

print('{:.2f}'.format(media/cont))