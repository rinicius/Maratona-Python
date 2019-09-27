op = input('insira sua operação matemática')

num1 = float(input('Insira o primeiro valor'))
num2 = float(input('Insira o segundo valor'))

print({
    '+': num1 + num2,
    '-': num1 - num2,
    '/': num1 / num2,
    '*': num1 * num2,
    }[op])
