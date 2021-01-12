# Henrique Lima
# Calculadora utilizando funções

print("Soma .................... +")

print("Subtração ............. -")

print("Multiplicação......... *")

print("Divisão................... /")

print("Sair ....................... 0 \n")

def adicao(a, b):
    result = a + b
    return result

def subtracao(a, b):
    result = a - b
    return result

def multiplicacao(a, b):
    result = a * b
    return result

def divisao(a, b):
    result = a / b
    return result

def main():
    c = 0
    while c == 0:
        entrada = input("Selecione a opção desejada: ")
        while entrada != "+" and entrada != "-" and entrada != "*" and entrada != "/" and entrada != "0":
            entrada = input("Opção inválida! Selecione a opção desejada: ")
        if entrada == "+":
            n1 = float(input("Digite um número: "))
            n2 = float(input("Digite outro número: "))
            print("A soma dos números é: " ,adicao(n1, n2))
        elif entrada == "-":
            n1 = float(input("Digite um número: "))
            n2 = float(input("Digite outro número: "))
            print("A subtração dos números é: " ,subtracao(n1, n2))
        elif entrada == "*":
            n1 = float(input("Digite um número: "))
            n2 = float(input("Digite outro número: "))
            print("A multiplicação dos números é: " ,multiplicacao(n1, n2))
        elif entrada == "/":
            n1 = float(input("Digite um número: "))
            n2 = float(input("Digite outro número: "))
            while n2 == 0:
                n2 = float(input("Impossível divisão por zero! Digite outro número: "))   
            print("A divisão dos números é: " ,divisao(n1, n2))
        elif entrada == "0":
            print("Programa encerrado")
            c = c + 1
            
main()
    
    
