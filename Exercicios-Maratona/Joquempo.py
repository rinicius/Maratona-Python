while True:
    
    jogadas = ['tesoura', 'papel', 'pedra']   
    joao = pedro = 0 

    qtdJogadas = int(input())

    if qtdJogadas == 0:
        break

    for i in range(0, qtdJogadas):
        
        entrada = input()

        pontosJogador1 = pontosJogador2 = 0
        
        if entrada.split()[1] == jogadas[0]:

            if entrada.split()[3] == jogadas[1]:
                pontosJogador1 = 1

            else:
                pontosJogador2 = 1
                
        elif entrada.split()[1] == jogadas[1]:

            if entrada.split()[3] == jogadas[0]:
                pontosJogador1 = 1

            else:
                pontosJogador2 = 1

        elif entrada.split()[1] == jogadas[2]:

            if entrada.split()[3] == jogadas[0]:
                pontosJogador2 = 1

            else:
                pontosJogador1 = 1

        if 'Joao' == entrada.split()[0]:

            if pontosJogador1 > pontosJogador2:
                joao += 1
                    
            elif pontosJogador1 < pontosJogador2:
                pedro += 1
        
        else:

            if pontosJogador1 > pontosJogador2:
                pedro += 1
                    
            elif pontosJogador1 < pontosJogador2:
                joao += 1

    if joao > pedro:
        print(f"Joao {joao}")

    elif pedro > joao:
        print(f"Pedro {pedro}")

    else:
        print("Empate")
        
# Joao tesoura Pedro pedra
# Pedro tesoura Joao pedra
# Papel > Pedra
# Pedra > Tesoura
# Tesoura > Papel
# Empates