#Henrique Lima

lista = []

def entrada():
    for i in range(4):
        nota = float(input("Digite a nota: " ))
        lista.append(nota)

def saida():
    soma = 0
    for i in range(len(lista)):
        soma = soma + lista[i]
    media = soma/len(lista)
    print("Sua média é: " ,media)
                                       
def main():
    entrada()
    saida()

main()
        
       
        
