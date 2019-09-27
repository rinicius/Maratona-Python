produto = input('Insira o valor e o estado que ele será vendido\n')
produto = produto.split()
produto[0] = float(produto[0])

valor, estado = produto

mg = 0.07
sp = 0.12
rj = 0.15
ms = 0.08

while True:
    if estado != 'mg' and estado != 'sp' and estado != 'rj' and estado !='ms':
        print('Insira o estado correto\n')
        estado = input()
    elif estado == 'mg':
        estado = mg
        break
    elif estado == 'sp':
        estado = sp
        break
    elif estado == 'rj':
        estado = rj
        break
    elif estado == 'ms':
        estado = ms
        break

print(f'O valor final é de {valor * estado + valor}')     