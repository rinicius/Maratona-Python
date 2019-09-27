horario = input('Insira o horário')
horario = horario.split(':')
horario = [int(i) for i in horario]

minutos = 0

if len(horario) == 3:
    minutos += horario[0] * 60
    minutos += horario[1]
    minutos += horario[2] / 60

elif len(horario) == 3:
    minutos += horario[0]
    minutos += horario[1] / 60

else:
    minutos += horario[2] / 60

print(minutos)
