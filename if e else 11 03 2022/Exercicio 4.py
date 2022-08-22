#Faça um programa que apresente se o número que o usuário digitou é divisível por 3 e por 5 ao mesmo tempo.

num = int (input("Digite um número inteiro:"))

if (num % 3) == 0 and (num % 5)  == 0:
    print ("Número é divisivel por 3 e 5")
else:
    print ("Não é divisivel por 3 e 5")
