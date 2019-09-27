def soma(num1, num2):
    return num1 + num2


def diferenca(num1, num2):
    if num1 > num2:
        return num1 - num2
    else:
        return num2 - num1


def produto(num1, num2):
    return num1 * num2


def divisao(num1, num2):
    if num1 == 0 or num2 == 0:
        return 'O denominador nao pode ser zero'
    else:
        return num1 / num2


escolha = input('Escolha: \nsoma\ndiferenca\nproduto\ndivisao\n')

num1 = float(input('insira o primeiro valor'))
num2 = float(input('insira o segundo valor'))

print({
    'soma': soma(num1, num2),
    'diferenca': diferenca(num1, num2),
    'produto': diferenca(num1, num2),
    'divisao': divisao(num1, num2),
}[escolha])

