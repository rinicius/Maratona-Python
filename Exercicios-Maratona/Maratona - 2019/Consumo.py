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
qtd = int(input('Insira a qtd'))
carro = list()
media = 0
cont = 0


    
for i in range(0, qtd):
    arr = input('Placa, km, litros')
    cont += 1
    if arr == 1:
        break
    else:
        carro.append(arr)



for i in range(len(carro)):

    placa, km, litro = carro[i].split()
    km = float(km)
    litro = float(litro)
    media += km/litro

media = media / qtd


print(media)
