#Autor: Henrique Lima
def maximo(x, y):
    if x > y:
        return x
    else:
        return y

def main():
    n1 = int(input("Digite o primeiro número: "))
    n2 = int(input("Digite o segundo número: "))
    print(maximo(n1, n2))
    

main()
    
