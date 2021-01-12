#Autor: Henrique Lima
def areaQuadrado(lado):
    area = lado * lado
    return area

def main():
    x = int(input("Digite o lado: "))
    print("Área do quadrado: " ,areaQuadrado(x))

main()
    
