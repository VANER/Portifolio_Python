#Escreva um código que receba um número de segundos e converta este número em horas, minutos e segundos. Escreva também um código que faça o contrário. 

print ('CONVERSOR DE SEGUNDOS PARA  H: M: S')
total_segundos = int(input('Informe o número total de segundos: ')) #Variavel recebe o numero total dr segundos digitado pelo usuario.
minutos  = total_segundos // 60 #Divisao inteiro
segundos = total_segundos % 60 #Resto da divisao
horas = minutos // 60 
minutos = minutos % 60
print (total_segundos, 'segundos é igual a: ', horas,  ':', minutos,  ':', segundos) #Escreve na tela  o resultado da conversao dos segundos