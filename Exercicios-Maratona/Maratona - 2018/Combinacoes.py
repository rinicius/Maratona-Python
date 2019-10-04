"""AAAXYZBBBBMNOCCCCCZ = 90"""

while True:
    pontos = 0
    entrada = input()
    listai = list()
    if entrada == '0':
        break
    else:
        lista = list(entrada)

        for i in lista:
            if i not in listai:
                if lista.count(i) == 3:
                    pontos += 10
                    listai.append(i)
                elif lista.count(i) == 4:
                    pontos += 30
                    listai.append(i)
                elif lista.count(i) == 5:
                    pontos += 50
                    listai.append(i)
                else:
                    pass
        print(pontos)
