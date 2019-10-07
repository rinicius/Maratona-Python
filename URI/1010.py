peca1 = list(map(float, input().split()))
peca2 = list(map(float, input().split()))


total = (peca1[1] * peca1[2]) + (peca2[1] * peca2[2])

print('VALOR A PAGAR: R$ {:.2f}'.format(total))
