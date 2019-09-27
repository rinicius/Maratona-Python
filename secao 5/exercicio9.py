
salarioemprestimo = input('Insira o salario e o emprestimo\n')
salarioemprestimo = salarioemprestimo.split()
salarioemprestimo = [float(i) for i in salarioemprestimo]

if salarioemprestimo[1] > (salarioemprestimo[0] * 0.2):
    print('Emprestimo nao concedido')
else:
    print('Emprestimo concedido')
