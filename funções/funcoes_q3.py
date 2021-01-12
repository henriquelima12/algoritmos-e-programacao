#Henrique Lima

def somaImposto(taxaImposto, custo):
    valorVenda = custo + (custo * (taxaImposto / 100))
    return valorVenda

def main():
    t = int(input("Digite a taxa do imposto(%): "))
    c = float(input("Digite o custo do item: "))
    print("O valor da venda é: " ,somaImposto(t, c))

main()
