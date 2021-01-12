#Autor: Henrique Lima
#Data: 25/03/2020
#Receber preço de etiqueta, código do produto e calcular o valor a ser pago.

preco = float(input("Digite o preço do produto: "))
codigo = int(input("Digite o código de pagamento: "))

if codigo == 1:
    print("O valor do produto é de: " ,(preco * 0.90), "R$")
elif codigo == 2:
    print("O valor do produto é de: " ,(preco * 0.95), "R$")
elif codigo == 3:
    print("O valor do produto é de: " ,preco, "R$")
elif codigo == 4:
    print("O valor do produto é de: %.2f" %(preco * 1.10), "R$")
else:
    print("Código inválido")

    
