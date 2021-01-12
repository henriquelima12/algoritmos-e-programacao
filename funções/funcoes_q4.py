#Henrique Lima

def exibeMsg():
    print("Este programa permite ao usuário converter uma faixa de temperatura")
    print("de Fahrenheit para Celsius e de Celsius para Fahrenheit. \n")

def getConvertTo():
    entrada = input("Digite qual temperatura será convertida: ")
    while entrada != "F" and entrada != "C":
        entrada = input("Entrada inválida! Digite a temperatura a ser convertida: ")
    return entrada

def exibeFahrenheitTOCelsius(f):
    novaTemperatura = (f - 32) / 1.8
    return novaTemperatura

def exibeCelsiusTOFahrenheit(c):
    novaTemperatura = (c * 1.8) + 32
    return novaTemperatura

def main():
    exibeMsg()
    escolha = getConvertTo()

    if escolha == "F":
        temp = float(input("Digite a temperatura em fahrenheit a ser convertida para celsius: "))
        print("A temperatura em celsius é: " ,exibeFahrenheitTOCelsius(temp))
    elif escolha == "C":
        temp = float(input("Digite a temperatura em celsius a ser convertida para farenheit: "))
        print("A temperatura em fahrenheit é: " ,exibeCelsiusTOFahrenheit(temp))

main()
        

    
    
