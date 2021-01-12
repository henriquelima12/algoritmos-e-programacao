#Autor: Henrique Lima
#Data: 25/03/2020
#Ler número inteiro de três digitos e exibir se o algarismo da dezena é ímpar ou par.

n1 = int(input("Digite um número inteiro de três digitos: "))

if ((n1 // 10 ) % 10 ) % 2 == 0:
    print("O algarismo da dezena é par")
else:
    print("O algarismo da dezena é ímpar")
