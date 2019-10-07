while True:
    cont = 0
    try:
        qtd, altmin, altmax = map(int, input().split())
    except:
        break
    
    for i in range(qtd):
        alt = int(input())
        if alt >= altmin and alt <= altmax:
            cont += 1
        else:
            pass
    
    print(cont)