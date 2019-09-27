while True:
    a = ''
    a = input('Inserir um numero inteiro')
    a = list(a)
    a = [int(i) for i in a]
    a = sum(a)
    print(a)

    if input('Deseja continuar?') == 'sim':
        pass
    else:
        break
