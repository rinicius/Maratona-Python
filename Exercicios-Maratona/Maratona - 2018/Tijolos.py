import math
""" A L C P V, onde: 
altura do tijolo (5cm <= A <= 20cm), 
largura do tijolo (5cm <= L <= 20cm), 
comprimento do tijolo (15cm <= C <= 50cm) 
perímetro do cômodo (8m <= P <= 200m) em metros 
valor do milheiro (R$ 50 <= V <= R$ 2670). 

A entrada terminará com uma linha com um único número zero e deverá ser lida da entrada padrão. 
 """


while True:
    entrada = input()
    if entrada == '0':
        break

    altura = float(entrada.split()[0])
    largura = float(entrada.split()[1])
    comprimento = float(entrada.split()[2])
    perimetrocomodo = float(entrada.split()[3])
    valorm = float(entrada.split()[4])

    tjpormetro = 1
    tjpormetro /= (comprimento/100 + 0.01) * (altura/100 + 0.01)
    tjpormetro = math.floor(tjpormetro)
    tjpormetro = '{:.0f}'.format(tjpormetro)

    area = perimetrocomodo * 2.8
    tjtotal = round((area * int(tjpormetro)), 1)


    # valor é para cada 1000 tijolos
    custototal = tjtotal / 1000
    custototal *= valorm
    custototal = math.floor(custototal)




    print (tjpormetro, math.floor(tjtotal), custototal)
 