#Henrique Lima

num = [30, 40, 60, 7, 8, 50]

def contar():
    return len(num)

def somar():
    return sum(num)

def media():
    return somar() / contar()

def maior():
    return max(num)

def menor():
    return min(num)

def main():
    print("N° de elementos: " ,contar())
    print("Soma dos elementos: " ,somar())
    print("Média dos elementos: " ,media())
    print("Maior número: " ,maior())
    print("Menor número: " ,menor())

main()
