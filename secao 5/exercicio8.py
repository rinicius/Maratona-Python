nota = []
i = 0
while i < 2:
    nota.append(float(input(f'Insira a {i+1}º nota')))
    if (nota[i] < 0.0) or (nota[i] > 10.0):
        nota[i] = 0
        i = 0
        break
    else:
        i += 1


print(nota)