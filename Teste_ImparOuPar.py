#Testar se um número é ímpar ou par, sem usar o operador %. 

print ('TESTE NUMERO IMPAR OU PAR')
n = int(input('Informe um número: '))

#Estrutura de decisão
if n // 2 * 2 - n == 0: #Na divisão tem que usar o operador de divisão inteira (//).
    print ('O número ', n, ' é par.') #Condição verdadeira
else:
     print ('O número ', n, ' é ímpar.') #Condição falsa