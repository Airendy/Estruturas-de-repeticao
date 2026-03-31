#Crie um programa que peça ao usuario para digitar 10 números inteiros
#Use laço for para percorrer a lista
#Para cada número classifique como maior que 10, igual a 10 e menor que 10.

numeros = []
for i in range(10):
 num = int(input(f"Digite o número: "))
 numeros.append(num)


for num in numeros:
 if num > 10:
  print(f"{num} é maior que 10 ")
 elif num == 10:
  print(f"{nume} é igual a 10 ") 
 else:
  print(f"{num} é menor que 10 ")