area = list(map(float, input().split()))

print('TRIANGULO: {:.3f}'.format((area[0] * area[2]) / 2))
print('CIRCULO: {:.3f}'.format(3.14159 * area[2]**2))
print('TRAPEZIO: {:.3f}'.format(((area[0] + area[1]) * area[2]) / 2))
print('QUADRADO: {:.3f}'.format(area[1]**2))
print('RETANGULO: {:.3f}'.format(area[0] * area[1]))