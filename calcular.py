print("Soma ..................... +")
print("Subtração ................ -")
print("Multiplicação............. *")
print("Divisão................... /")
print("Sair ..................... 0")

ct = 0

print("Escolha +, -, *, / ou 0(Caso queira sair do programa)")
while ct == 0:
    entrada = input("Digite uma das opções: ")
    if entrada == "0":
        print("Programa encerrado")
        ct = ct + 1
    elif entrada == "+":
        num1 = int(input("Digite um número inteiro: "))
        num2 = int(input("Digite um número inteiro: "))
        resultado = num1 + num2
        print("Resultado: " ,resultado)
    elif entrada == "-":
        num1 = int(input("Digite um número inteiro: "))
        num2 = int(input("Digite um número inteiro: "))
        resultado = num1 - num2
        print("Resultado: " ,resultado)
    elif entrada == "*":
        num1 = int(input("Digite um número inteiro: "))
        num2 = int(input("Digite um número inteiro: "))
        resultado = num1 * num2
        print("Resultado: " ,resultado)
    elif entrada == "/":
        num1 = int(input("Digite um número inteiro: "))
        num2 = int(input("Digite um número inteiro: "))
        resultado = num1 / num2
        print("Resultado: " ,resultado)
    elif entrada != "+" or "-" or "*" or "/" and "0":
        print("Opção inválida")
        
        





    
    
    
        

        




