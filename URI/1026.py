while True:
    try:
        valor1, valor2 = map(int, input().split())
        print(int(valor1)^int(valor2))
    except:
        break