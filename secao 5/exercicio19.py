a = float(input('Insira o VALOR'))

if a % 3 == 0 and a % 5 != 0:
    print('o numero é divisivel por tres')
elif a % 3 != 0 and a % 5 == 0:
    print('o numero é divisel por cinco')
elif a % 3 == 0 and a % 5 == 0:
    print('divisivel pelos dois')
else:
    print('divisivel por nenhum')