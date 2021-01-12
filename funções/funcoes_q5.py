#Henrique Lima

def valorPagamento(valorPrestacao, diasAtraso):
    valorTotal = (valorPrestacao + (valorPrestacao * 0.03) + (diasAtraso * 0.001))
    return valorTotal
    
def main():
    q = 0
    v = 0
    a = 0
    while a < 1:
        vP = float(input("Digite o valor da prestação: "))
        if vP == 0:
            a = a + 1
            print("Programa encerrado")    
        elif vP != 0:
            dA = int(input("Digite a quantidade de dias de atraso: "))
            if dA == 0:
                vT = vP
            else:
                vT = valorPagamento(vP, dA)
            print("O valor a ser pago é: " ,(format(vT, ".2f")), "R$")
            q = q + 1
            v = v + vT
        
    print("A quantidade total de prestações é: " ,q)
    print("O valor total de prestações pagas é de: " ,(format(v, ".2f")), "R$")

main()

    
