#Autor: Henrique Lima
def entrada():
    n = int(input("Digite um número: "))
    while n<=0:
        n = int(input("Digite um número: "))
    return n

def contaDivisor(n):
    ndiv = 0
    for i in range(1, n+1):
        resto = n % i
        if resto == 0:
            ndiv = ndiv + 1
    return ndiv

def main():
    n = entrada()
    print(contaDivisor(n))

main()
    
