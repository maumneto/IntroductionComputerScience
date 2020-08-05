# Crie um programa na linguagem Python que lê do usuário a duração em 
# dias, horas, minutos e segundos. Calcule e apresente o número total de segundos dessa 
# duração fornecida do usuário. 

dias = int(input('Digite o total de dias: '))
horas =  int(input('Digite o total de horas: '))
minutos = int(input('Digite o total de minutos: '))
segundos = int(input('Digite o total de segundos: '))

dias_para_segundos = dias * 24 * 60 * 60
horas_para_segundos = horas * 60 * 60
minutos_para_segundos = minutos * 60

total_segundos = dias_para_segundos + horas_para_segundos + minutos_para_segundos + segundos
print('Total em Segundos = %d segundos' % total_segundos)