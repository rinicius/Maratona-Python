lista1 = input('insira os valores basemaior, basemenor e altura')
lista1 = lista1.split()
lista1 = [float(i) for i in lista1]

basemaior, basemenor, altura = lista1

total = (basemaior + basemenor) / altura

print(total)
