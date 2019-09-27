notas = input('Insira os numeros abaixo\n')
notas = notas.split()
notas = [int(i) for i in notas]

media = sum(notas)
media = media / len(notas)

print(media)
