"""
1 2 3 4 5 6 7 8 9 10 // 1
1 3 5 7 9
1 3 7 9
1 3 7


1 3 8 9 11 12 13 14 15 26 29 38 44 49 50 55 56 57 58 66 77 88 99 105 123 // 19

1 8 11 13 15 29 44 50 56 58 77 99 123 // 10

1 8 13 15 44 50 58 77 123 // 7

1 8 13 44 50 58 123 // 6

1 8 13 44 58 123 // 5

1 8 13 44 58 // 4


"""
import math
while True:
    try:
        qtd = int(input())
        ordem = list(map(int,input().split()))
        inteiro = int(input())

        if ordem.index(inteiro) == 0:
            print('Y')
        else:

            indexin = ordem.index(inteiro) - math.floor(ordem.index(inteiro)/2)
            i = 2

            while True:
                i += 1
                if indexin/i > 1:
                    indexin = indexin - math.floor(indexin/i)
                else:
                    break

            if indexin >= i:
                print('Y')
            else:
                print('N')

    except:
        break