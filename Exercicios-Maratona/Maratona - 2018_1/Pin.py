"""
- Se 1 <= N <= 20 e for múltiplo de 4 ou;
  - Se 21 <= N <= 50 e for múltiplo de 3 ou;
    - Se 51 <= N <= 70 e for ímpar ou;
      - Se N > 70 e for par. 
"""

numeros = list()
while True:
    entrada = int(input())
    if entrada == 0:
        break
    else:
        numeros.append(entrada)



for i in range(len(numeros)):
    if numeros[i] >= 1 and numeros[i] <= 20:
        if numeros[i] % 4 == 0:
            numeros[i] = 'PIN'
        else:
            pass
    elif numeros[i] >= 21 and numeros[i] <= 50:
        if numeros[i] % 3 == 0:
            numeros[i] = 'PIN'
        else:
            pass
    elif numeros[i] >= 51 and numeros[i] <= 70:
        if numeros[i] % 2 != 0:
            numeros[i] = 'PIN'
        else:
            pass
    elif numeros[i] >= 71:
        if numeros[i] % 2 == 0:
            numeros[i] = 'PIN'
        else:
            pass

for i in numeros:
    print(i)