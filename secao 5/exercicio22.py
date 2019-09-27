lista1 = input('Escreva a idade e  tempo de serviço')
lista1 = lista1.split()
lista1 = [int(i) for i in lista1]

idade, tempodeservico = lista1

if idade >= 60 and tempodeservico >= 25:
    print('Pode se aposentar')
elif idade >= 65:
    print('Pode se aposentar')
elif tempodeservico >= 30:
    print('Pode se aposentar')
else:
    print('Não pode se aposentar')