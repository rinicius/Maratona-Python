#!/usr/bin/env python3

# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

import sys

if __name__ == "__main__":
    qtdePrimos = 8
    n = 1

    primos = []
    fatoriais = []
    c = 1

    while c <= qtdePrimos:
        n += 1
        r = True
        for i in range(2, int(n / 2)+1) :
            if n % i == 0:
                r = False
                break
        if r:
            primos.append(n)
            c += 1

    for f in range(0,qtdePrimos):
        fat = 1
        for x in range(1,primos[f]+1):
            fat *= x
        fatoriais.append(fat)
    
    while True:
        linha = input()
    
        if linha in '0':
            break
                
        f = int(linha)

        saida = ""
        
        for x in range(0,qtdePrimos):
            if f == fatoriais[x]:
                saida = str(primos[x]) + "! = "
                for y in range(primos[x],0,-1):
                    saida += str(y)+" "
                    if y>1:
                        saida += ". "
                    else:
                        saida += "="
                            
                print(saida,fatoriais[x])

    sys.exit()
    