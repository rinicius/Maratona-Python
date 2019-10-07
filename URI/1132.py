x = list()
x.append(int(input()))
x.append(int(input()))

soma = 0

for i in range(min(x), max(x)+1):
    if i % 13 != 0:
        soma += i



print(soma)