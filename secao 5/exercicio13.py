nota = input('Insira as 3 notas')
nota = nota.split()
nota = [float(i) for i in nota]

media = (nota[0] * 1 + nota[1] * 1 + nota[2] * 2) / len(nota)

print('passou' if media > 60 else 'reprovou')
