#Autor: Henrique Lima
#Data: 25/03/2020
#Ler o número de maçãs compradas e receber o valor da compra.

qtd_macas = int(input("Digite o número de maças que foram compradas: "))

if qtd_macas < 12:
    print(" O valor total da compra é de: %.2f" %(qtd_macas * 1.30), "R$")
else:
    print(" O valor total da compra é de: %.2f " %(qtd_macas * 1.00), "R$")
          
