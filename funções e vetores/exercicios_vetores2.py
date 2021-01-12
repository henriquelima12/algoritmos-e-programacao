#Henrique Lima

#Faça um Programa que leia um vetor de 5 números inteiros.
#Mostre a soma, a multiplicação e os números.

lista = []

def entrada():
    for i in range(5):
        num = int(input("Adicione um número: "))
        lista.append(num)
    print("Lista: " ,lista)

def soma():
    print("Soma dos valores da lista: " ,sum(lista))

def multiplicacao():
    a = 1
    for i in lista:
        a = a * i
    print("Multiplicação dos valores da lista: " ,a )

def main():
    entrada()
    soma()
    multiplicacao()

main()
    
        
        
    
