a = 1
x = 0
f = 0
p = 0

while a <= 10:
    turma = input("Digite a identificação da turma: ")
    numero_alunos = int(input("Digite o número de alunos dessa turma: "))
    while numero_alunos <20 or numero_alunos >100:
        numero_alunos = int(input("Digite o número de alunos dessa turma: "))
    
    while x < numero_alunos:
        matricula = int(input("Digite o número de matricula do aluno: "))
        while matricula <1000 or matricula >9999:
            matricula = int(input("Digite o número de matricula do aluno: "))
        situacao = input("Digite apenas ""S"" se o aluno esteve presente ou apenas ""N"" se o aluno faltou: ")
        while situacao != "S" and situacao != "N":
            situacao = input("Digite apenas ""S"" se o aluno esteve presente ou apenas ""N"" se o aluno faltou: ")

        if situacao == "N":
            f = f + 1
        
        x = x + 1
        
    a = a + 1
    
    porcentagem_ausencia = (f * 100) / numero_alunos

    print("Turma " ,turma, "," ,porcentagem_ausencia, "% dos alunos faltaram a avaliação \n")

    if porcentagem_ausencia > 10:
        p = p + 1
        
    x = 0
    
    f = 0
    
print(p, "turmas tiveram mais de 10% de ausência.")
    

    
    
    




