print('Insira 6 valores na linha abaixo:')
a = input()
a = a.split()

i = 0
while True:
    print(a[i])
    i += 1
    if i >= len(a):
        break


