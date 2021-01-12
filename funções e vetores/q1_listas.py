#Henrique Lima

lista = []

def entrada():
    for i in range(5):
        num = int(input("Adicione um número: "))
        lista.append(num)

def saida():
    print(lista)

def main():
    entrada()
    saida()

main()
