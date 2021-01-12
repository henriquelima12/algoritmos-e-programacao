#Autor: Henrique Lima
#Data: 25/03/2020
#Ler dois números distintos e apresentar o quadrado do maior número.

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

if num1 > num2:
    print("O quadrado do maior número é: " ,(num1**2))
else:
    print("O quadrado do maior número é: " ,(num2**2))
