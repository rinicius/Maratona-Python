nomes = ['Ana', 'Solomon', 'Junior']
notas = [5, 10, 1]

nomes, notas = list(zip(*sorted(zip(nomes, notas), key=lambda x:x[1])))
print(nomes)
print(notas)