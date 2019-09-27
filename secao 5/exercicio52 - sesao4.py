def porcentagemdecada(num1, num2, num3):
    porcentagemtotal = num1 + num2 + num3

    num1 = 100 * num1 / porcentagemtotal
    num2 = 100 * num2 / porcentagemtotal
    num3 = 100 * num3 / porcentagemtotal
    return [num1, num2, num3]


def porcentagemtotal(num1, num2, num3, premio):
    num1 = num1 * premio / 100
    num2 = num2 * premio / 100
    num3 = num3 * premio / 100
    return num1, num2, num3


array = input('Insira quanto cada amigo investiu\n')
array = array.split()
array = [int(i) for i in array]

premio = float(input('Insira o valor do prêmio\n'))

listaporcento = porcentagemdecada(array[0], array[1], array[2])

cadaganhador = porcentagemtotal(listaporcento[0], listaporcento[1], listaporcento[2], premio)

print(f'1º ganhador: {cadaganhador[0]}'
      f'2º ganhador: {cadaganhador[1]}'
      f'3º ganhador: {cadaganhador[2]}')

