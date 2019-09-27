aluno = input('Insira as três notas')
aluno = aluno.split()
aluno = [float(i) for i in aluno]

media = (aluno[0] * 2 + aluno[1] * 3 + aluno[2] * 5) / len(aluno)

if media <= 2.9:
    print('passou')
elif media < 4.9:
    print('reprovado')
else:
    print('aprovado')

