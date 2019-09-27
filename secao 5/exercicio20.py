a = int(input('Primeiro segmento: '))
b = int(input('Segundo segmento: '))
c = int(input('Terceiro segmento: '))

if a == b == c:
    print('Triângulo Equilátero')

elif a == b or a == c or b == c:
    print('Triângulo Isósceles')

elif a != b != c != a:
    print('Triângulo Escaleno')

else:
    print('Não é possivel formar um triângulo')