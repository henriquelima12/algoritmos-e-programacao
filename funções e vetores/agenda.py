#Henrique Lima

agenda = []

def cadastrar1():
    nome = input("Digite o nome de um amigo que você deseja adicionar no final da lista: ")
    agenda.append(nome)

def mostrar2():
    print(agenda)

def cadastrar3():
    nome = input("Digite o nome de um amigo que você deseja adicionar ao início da lista: ")
    agenda.insert(0, nome)

def remover4():
    nome = input("Digite o nome que você quer remover: ")
    a = nome in agenda
    
    if a == False:
        print("Nome não pertence à lista. Adicione um nome")
    else:
        del agenda[agenda.index(nome)]

def substituir5():
    nome = input("Digite o nome que você deseja substituir na lista: ")
    novoNome = input("Digite o nome de um amigo que você deseja acrescentar à lista: ")
    agenda[agenda.index(nome)] = novoNome
    
def mostrar6():
    print("O número de nomes cadastrados na lista: " ,len(agenda))

def ordenar7():
    agenda.sort()
    print(agenda, "\n")

def menu():

    print("\n(1)Cadastrar um amigo (no final da lista)")

    print("(2)Mostrar os nomes de todos os amigos")

    print("(3)Cadastrar um amigo (no início da lista)")

    print("(4)Remover um nome")

    print("(5)Substituir um nome")

    print("(6)Mostrar o número total de amigos cadastrados")

    print("(7)Colocar os nomes dos amigos em ordem alfabética")

    print("(8)Sair do programa")

    escolha = int(input("\nEscolha uma opção: "))
    return escolha

def main():
    c = 0
    while c == 0:
        op = menu()
        while op != 1 and op != 2 and op != 3 and op != 4 and op != 5 and op != 6 and op != 7 and op != 8:
            print("Escolha inválida")
            op = menu()
            
        if op ==1:
            cadastrar1()
        elif op == 2:
            mostrar2()
        elif op == 3:
            cadastrar3()
        elif op == 4:
            remover4()
        elif op == 5:
            substituir5()
        elif op == 6:
            mostrar6()
        elif op == 7:
            ordenar7()
        elif op == 8:
            print("Programa finalizado!")
            c = c + 1

main()



            
    
    
