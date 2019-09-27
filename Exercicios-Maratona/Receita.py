"""
Receita de Bolo

Receita de Milho:

['Milho verde', 'Oleo vegetal', 'Acucar', 'Fuba', 'Ovos', 'Farinha de trigo', 'Coco ralado', 'Fermento em po', 'Leite de coco']
[200 kg, 200 L, 250 kg, 200 kg, 4, 15 kg, 15 kg, 5 kg, 0 L]

Receita de Coco:

['Milho verde', 'Oleo vegetal', 'Acucar', 'Fuba', 'Ovos', 'Farinha de trigo', 'Coco ralado', 'Fermento em po', 'Leite de coco']
[0 kg, 120 L, 360 kg, 0 kg, 4, 240 kg, 100 kg, 10kg , 200 L]

1
10 10
Milho verde 2Kg
Oleo vegetal 3L
Acucar 6Kg
Fuba 2Kg
Ovos 80
Farinha de trigo 2Kg
Coco ralado 1Kg
Fermento em po 0Kg
Leite de coco 2L
"""

dias = int(input('Insira os dias'))
bolo = input('Bolo de Milho e Coco')
bolom, boloc = bolo.split()

bolom = int(bolom)
boloc = int(boloc)

ingredientesm = {'MilhoVerde': 200, 'OleoVegetal': 200, 'Acucar': 250, 'Fuba': 200, 'Ovos': 4, 'FarinhaDeTrigo': 15, 'CocoRalado': 15, 'Fermento': 5, 'LeiteDeCoco': 0}
ingredientesc = {'MilhoVerde': 0, 'OleoVegetal': 120, 'Acucar': 360, 'Fuba': 0, 'Ovos': 4, 'FarinhaDeTrigo': 240, 'CocoRalado': 100, 'Fermento': 10, 'LeiteDeCoco': 200}

for i in ingredientesm:
    if i == 'Ovos':
        print(f'Ingrediente: {i}, Quantia final: {((ingredientesm[i]*(bolom+boloc)) * dias)}')
    elif i == 'OleoVegetal' or i == 'LeiteDeCoco':
        print(f'Ingrediente: {i}, Quantia final: {((ingredientesm[i]*(bolom+boloc)) * dias)/1000}L')
    else:
        print(f'Ingrediente: {i}, Quantia final: {((ingredientesm[i]*(bolom+boloc)) * dias)/1000}KG')

