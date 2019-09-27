longlat = input()
long, lat = longlat.split(';')

pos = None

if long[0] == '-':
    pos = 'Sul'
elif long[0] == '0':
    pos = 'Equador'
else:
    pos = 'Norte'

if lat[0] == '-':
    pos += ' Oeste'
elif lat[0] == '0':
    pos += 'Greenwich'
else:
    pos += 'Leste'

print(pos)

