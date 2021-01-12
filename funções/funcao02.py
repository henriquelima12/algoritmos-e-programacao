#Autor: Henrique Lima
def multiplo(n1, n2):
    if n1 % n2 == 0:
        return True
    else:
        return False

def main():
    x = int(input("Digite o primeiro número: "))
    y = int(input("Digite o segundo número: "))
    print(multiplo(x, y))

main()
    
