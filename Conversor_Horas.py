# Escreva um código que receba um número de H: M: S  (horas, minutie e segundos) e converta este número em segundos..
print ('CONVERSOR DE H:M:S PARA SEGUNDOS')
print ('Informe as horas:')
horas = int(input('Horas: '))
minutos = int(input('Minutos: '))
segundos = int(input('Segundos: '))
total_segundos = horas * 60 * 60 + minutos * 60 + segundos
print ('O total dw segundos é: ' , total_segundos)