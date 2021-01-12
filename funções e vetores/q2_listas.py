#Henrique Lima

lista = []

def entrada():
    for i in range(10):
        n = int(input("Adicione um número: "))
        lista.append(n)

def saida():
    print(lista)

def main():
    entrada()
    lista.reverse()
    saida()

main()
        


    
    
