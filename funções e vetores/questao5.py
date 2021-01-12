#Henrique Lima

lista = []

def entrada():
    for i in range(10):
        nota1 = float(input("Digite a nota 1: "))
        while nota1 < 0 or nota1 > 10:
            nota1 = float(input("Inválido! Digite a nota 1: "))

        nota2 = float(input("Digite a nota 2: "))
        while nota2 < 0 or nota2 > 10:
            nota2 = float(input("Inválido! Digite a nota 2: "))

        nota3 = float(input("Digite a nota 3: "))
        while nota3 < 0 or nota3 > 10:
            nota3 = float(input("Inválido! Digite a nota 3: "))

        nota4 = float(input("Digite a nota 4: "))
        while nota4 < 0 or nota4 > 10:
            nota4 = float(input("Inválido! Digite a nota 4: "))
        print("\n")
            
        
        media = (nota1 + nota2 + nota3 + nota4) / 4
        lista.append(media)

def numAprovados():
    c = 0
    for i in lista:
        if i >= 7:
            c = c + 1
    return c

def main():
    entrada()
    print(lista)
    print("O número de alunos com média igual ou maior que 7 é : " ,numAprovados())

main()

    
