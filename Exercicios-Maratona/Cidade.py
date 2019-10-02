import collections

cidade = []
estado = []
premio = []
cidadeFinal = []
estadoFinal = []
premioFinal = []
lista = list()
cont = 0

while True:
    cont += 1
    entrada = input()

    if entrada == "0":
        break

    cidade.append(entrada.split(";")[3])
    estado.append(entrada.split(";")[4])
    premio.append(entrada.split(";")[5])

premio = [float(x) for x in premio]

for i in range(len(cidade)):
    for j in range(len(cidade)):
        if i == j:
            pass
        else:
            if cidade[i] == cidade[j]:
                if cidade[i] in cidadeFinal:
                    pass
                else:
                    premioFinal.append(premio[i] + premio[j])
                    cidadeFinal.append(cidade[i])
                    estadoFinal.append(estado[i])

for i in range(len(cidade)):
    if cidade[i] not in cidadeFinal:
        cidadeFinal.append(cidade[i])
        premioFinal.append(premio[i])
        estadoFinal.append(estado[i])

        

                
cont = 0
premioMaiores = []
premioMaiores = sorted(premioFinal)
ii = list()
for i in range(len(premioFinal)):

        if premioFinal[i] == premioMaiores[-1] or premioFinal[i] == premioMaiores[-2] or premioFinal[i] == premioMaiores[-3]:
            print('{} {} {:.0f}'.format(cidadeFinal[i], estadoFinal[i], premioFinal[i]))
  

# 1000;27/05/2009;1;Cidade A;SP;1000000.0
# 1002;15/04/2009;2;Cidade B;RJ;500000.5
# 1010;30/04/2009;2;Cidade C;MG;212000350.43
# 1020;31/05/2009;1;Cidade A;SP;3452789.67
# 1040;30/6/2009;1;Cidade D;AM;2431764.1
