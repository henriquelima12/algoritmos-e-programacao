import random

aposta = int(input("Digite o valor da sua aposta entre os números 2 e 12: "))

d1 = (random.randrange(1, 7))
d2 = (random.randrange(1, 7))

print ("Dado 1: " ,d1)
print ("Dado 2: " ,d2)

soma = d1 + d2

print("A soma dos dados é: " ,soma)

if (d1 + d2) == aposta:
    print("Você ganhou!")
else:
    print("Você perdeu!")

