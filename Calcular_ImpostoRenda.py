"""Calcular o imposto de renda de um salário considerando as seguintes alíquotas:
     Até R$ 1.903,98: isento; 
     De R$ 1.903,99 até R$ 2.826,65: 7,5%; 
     De R$ 2.826,66 até R$ 3.751,05: 15%; 
     De R$ 3.751,06 até R$ 4.664,68: 22,5%; 
     Acima de R$ 4.664,68: 27,5%."""
     
print('CALCULAR IMPOSTO DE RENDA SALÁRIO')
salario = float(input('Informe o salário: '))

#Estrura de decisão composta e  alinhada
if salario <= 1903.98:
    imposto = 0
elif salario <=2826.65:
    imposto = salario * 0.075
elif salario <= 3751.05:
    imposto = salario * 0.15
elif salario <= 4664.68:
    imposto = salario * 0.225
else:
    imposto = salario * 0.275
    
#Escreve o resultado na tela
print('O imposto de renda do salário é de R$', imposto)
    
    