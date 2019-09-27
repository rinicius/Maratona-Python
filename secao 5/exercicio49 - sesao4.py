import datetime

tempoatual = input('Insira a hora, minuto, segundo\n')
tempoatual = tempoatual.split()
tempoatual = [int(i) for i in tempoatual]

segundos = 0
segundos += tempoatual[0] * 3600
segundos += tempoatual[1] * 60
segundos += tempoatual[2]

tempoadd = int(input('Informe, em segundos, a duração\n'))

segundos += tempoadd

print(f'O horário final é: {datetime.timedelta(seconds=segundos)}')

