gabarito = list()

"""ABBEDCEAAC 4 
ABAEDCEDAB   
AEECDDEDAB 
AEEEDEEDAB 
ABBEDCEAAC 
ACEDBADEBC 1 
ACEDEADEDC 
0 
7 """

while True:
    entrada = input()
    if entrada == '0':
        break
    else:
        gabarito = list(entrada.split()[0])
        qtd = int(entrada.split()[1])

        acertos = 0
        erros = 0

        while qtd > 0:
            aluno = list(input())
            for i in range(len(aluno)):
                if aluno[i] == gabarito[i]:
                    acertos += 1
                else:
                    erros += 1

            print(acertos, acertos * 10, erros * 10)
            acertos = erros = 0
            qtd -= 1


