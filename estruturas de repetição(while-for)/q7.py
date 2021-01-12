x = 0
cta = 0
ctr = 0
n = int(input("Digite o número de alunos: "))
while n>200:
    n = int(input("Digite o número de alunos: "))
    
while x<n:
    n1 = float(input("Digite a nota 1: "))
    while n1 >10 or n1 < 0:
        n1 = float(input("Digite a nota 1: "))
              
        
    n2 = float(input("Digite a nota 2: "))
    while n2 >10 or n2 <0:
        n2 = float(input("Digite a nota 2: "))
       
        
    media = (n1 + n2) /2
    
    print("Média: " ,media)
    
    if media >= 6:
        cta = cta +1
    else:
        ctr = ctr + 1
    x = x + 1

print("O número de alunos aprovados é: " ,cta)
print("O número de alunos reprovados é: " ,ctr)
    


