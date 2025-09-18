#Receber três números e informar o maior deles. 

print ('TESTE MAIOR NUMERO') 
print ('Informe três números: ')

#Variaveis que recebe os dados informado pelo usuario.
n1 = int(input('Informe o 1° numero: '))
n2 = int(input('Informe o 2° numero: '))
n3 = int(input('Informe o 3° numero: '))

#Estruturw  de decisão composta
if (n1 > n2) and (n1 > n3):
    print ('O maior numero é: ', n1)
elif n2 > n3:
    print ('O maior numero é: ', n2)
else:
    print ('O maior numero é: ', n3)