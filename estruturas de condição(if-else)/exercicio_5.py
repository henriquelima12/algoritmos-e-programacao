#Autor: Henrique Lima
#Data: 25/03/2020
#Receber valor do produto e exibir valor da venda.

valor_produto = float(input("Digite o valor do produto: "))

if valor_produto < 20.00:
    print(" O valor da venda é de R$: " ,(valor_produto * 1.45))
else:
    print(" O valor da venda é de R$: " ,(valor_produto * 1.30))
          
