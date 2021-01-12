#Henrique Lima

lista = []

def entrada():
    for i in range(10):
        c = input("Digite um caractere: ")
        lista.append(c)

def contaVogais():
    cv = 0
    for x in lista:
        if x == "a" or x == "e" or x == "i" or x == "o" or x == "u":
            cv = cv + 1
    return cv

def contaConsoante():
    cc = 0
    for x in lista:
        cc = cc + 1
    return cc

def main():
    entrada()
    vogal = contaVogais()
    consoante = contaConsoante()
    print(lista)
    print("Quantidade de vogais: " ,vogal)
    print("Quantidade de consoantes: " ,(consoante - vogal))

main()
        
    
