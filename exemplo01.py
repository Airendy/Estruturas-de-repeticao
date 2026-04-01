#Solicitar o valor de uma compra
#Somar os valores informados
#Continuar pedindo valores até o usuário digitar 0
#Ao final, mostrar:Total das compras, quantidade de compras realizadas e valor médio das compras.

total_compras = 0
quantidade+compras = 0
valor = ''
   
while valor != '0':
 valor = float(input('Digite algo (ou "0" para encerrar): '))

 total_compras += valor
 quantidade_compras += 1

if quantidade_compras > 0:
 valor_medio = total_compras / quantidade_compras
else:
 valor_medio = 0 

print

 