nota = float(input("Digite a nota do aluno: "))
while nota <0 or nota >10:
    print("Inválido! Digite outra nota: ")
    nota = float(input("Digite a nota do aluno: "))
    
print("Nota válida: " ,nota)
    
