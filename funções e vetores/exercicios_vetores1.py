#Henrique Lima

#Faça um programa que leia 20 números inteiros e armazene-os num vetor.
#Armazene os números pares no vetor PAR e os números IMPARES no vetor impar.
#Imprima os três vetores.

lista = []
impares = []
pares = []

def entrada():
    for i in range(20):
        num = int(input("Adicione um número inteiro: "))
        lista.append(num)
    print("Lista: " ,lista)

def impar():
    for i in lista:
        if i % 2 != 0:
            impares.append(i)
    print("Lista com os números ímpares: " ,impares)

def par():
    for i in lista:
        if i % 2 == 0:
            pares.append(i)
    print("Lista com os números pares: " ,pares)

def main():
    entrada()
    impar()
    par()

main()
                  
