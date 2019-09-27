print("Eae")


def soma(numero1, numero2):
    return numero1 + numero2


print(soma(1, 2))

nome = "Vinicius"
print(nome.upper())
print(nome.lower())
print(nome.split())
print(list(nome))
print(nome[0])





def palindromo(nome11, nome22):

    nome11 = nome11.lower()
    nome22 = nome22.lower()

    nome11 = list(nome11)
    nome22 = list(nome22)

    cont = 0
    conti = 0
    for i in nome11:
        if nome11[cont] == nome22[len(nome22) - (cont + 1)]:
            cont += 1

    if cont == len(nome11) and cont == len(nome22):
        print('É um palindromo')
        print(cont)


palindromo("vinicius", "suiciniv")
