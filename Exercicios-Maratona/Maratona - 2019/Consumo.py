import math
"""

Consumo

Descubra os carros que estão abaixo da média da frota, exemplo:
FAE6871 600.00 50.00 = 12
EWE2202 450.00 45.00 = 10*
KAV1005 375.00 40.00 = 9.375*
LWR2204 535.00 35.00 = 15.29
MMN3345 650.00 55.00 = 11.9
NEI9875 465.00 50.00 = 9.3*

Media da frota = 11.3

Obs: *, o que devera aparecer como resultado.

"""
qtd = int(input())
carro = list()
media = 0
cont = 0

for i in range(0, qtd):
    qtd += 1
    arr = input()
    cont += 1
    if arr == 0:
        break
    else:
        carro.append(arr)

mediac = list()
mediaf = []
placal = list()
placaf = list()

for i in range(len(carro)):

    placa, km, litro = carro[i].split()
    km = float(km)
    litro = float(litro)
    mediac.append((km/litro))
    media += km/litro
    placal.append(placa)

media = media / qtd

valores, nomes = list(zip(*sorted(zip(mediac, placal))))
print(nomes[0])
print(nomes[1])
print(nomes[2])