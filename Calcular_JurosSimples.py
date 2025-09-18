#Considere a fórmula para cálculo de juros simples, J = (C × I × T) / 100, onde J, C, I e T correspondem a juros, capital, taxa e tempo, respectivamente. Construa um código que solicite ao usuário os valores de C, I e T e calcule J. 

print ('CALCULO DE JUROS SIMPLES')
print ('Informe os dados para o calculo do juros: ')
capital = float(input('Capital: '))
taxa = float(input('Taxa de juros: '))
tempo = float(input('Tempo: '))
juros = capital * taxa * tempo / 100
print (' O valor do juros é: R$ ', juros)