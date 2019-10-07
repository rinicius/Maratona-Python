entrada = input()
entrada = entrada.split()
entrada = [float(i) for i in entrada]

print('{:.0f} eh o maior'.format(max(entrada)))
