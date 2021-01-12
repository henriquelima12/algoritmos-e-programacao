#Autor: Henrique Lima
#Data: 25/03/2020
#Receber três valores de uma equação de segundo grau e calcular o valor do delta e das raízes reais.

import math

a = float(input("Digite o primeiro valor: "))
b = float(input("Digite o segundo valor: "))
c = float(input("Digite o terceiro valor: "))
delta = ((b ** 2) - (4 * a * c))
print ( " O valor de delta é: " ,delta)

if a == 0:
    print ("não existem raízes")
elif delta > 0 :
    d = math.sqrt(delta)
    print ("Raiz quadrada de delta: " ,d)
    r1 = (-b + d)/(2 * a)
    r2 = (-b - d)/(2 * a)
    print ( "As raízes da equação são: " ,r1, r2)
elif delta == 0 :
    d = math.sqrt(delta)
    print ("Raiz quadrada de delta é igual a 0")
    r3 = (-b)/(2 *  a)
    print ( "A raíz da equação é: " ,r3)
elif delta < 0:
    print(" Delta é menor do que zero ")

