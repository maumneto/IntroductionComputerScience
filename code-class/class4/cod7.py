# Desenvolva um programa que lê o tempo em segundos de um usuário. 
# Este programa deve apresentar o total de tempo na seguinte forma: DIA:HORAS:MINUTOS:SEGUNDOS. 
horas = 24
minutos = 60
segundos = 60

total_segundos = int(input('Digite o total de Segundos: '))

aux = total_segundos

dias = aux // (horas*minutos*segundos)
aux = int(aux % (horas*minutos*segundos))

horas = aux // (minutos*segundos)
aux = int(aux % (minutos*segundos))

minutos = aux // (segundos)
segundos = int(aux % (segundos))

print('TOTAL DE SEGUNDOS = %d -- %d DIAS: %d HORAS: %d MINUTOS: %d SEGUNDOS' % (total_segundos, dias, horas, minutos, segundos))

