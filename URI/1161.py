def fatorial(n):
    fatorial = 1
    while n > 0:
        fatorial *= n
        n = n - 1
    return fatorial


while True:
    try:
        x, y = map(int, input().split())

        print(fatorial(x) + fatorial(y))
    except:
        break
