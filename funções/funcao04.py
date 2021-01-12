#Autor: Henrique Lima
def areaTriangulo(base, altura):
    area = (base * altura)/2
    return area

def main():
    b = int(input("Digite a base: "))
    a = int(input("Digite a altura: "))
    print("Área do triângulo: " ,areaTriangulo(b, a))

main()
    
    
    
