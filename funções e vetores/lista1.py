#Henrique Lima

lista = []

def quantidade():
    n = int(input("Digite a quantidade de números: "))
    return n

def entrada(n):
    for i in range(n):
        num = int(input("Número: "))
        lista.append(num)

def saida():
    for x in lista:
        print("Valor: " ,x)

def main():
    a = quantidade()
    entrada(a)
    saida()

main()
