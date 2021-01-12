qtd_empregados = int(input("Digite a quantidade de empregados: "))
a = 0
m = 0
r = 0
f = 0

for i in range(1, qtd_empregados + 1, 1):
    nome = input("\nDigite o nome do empregado: ")
    print(nome)
    sexo = input("Digite o sexo do empregado: ")
    while sexo != "F" and sexo != "M" :
        sexo = input("Digite o sexo do empregado: ")
    print (sexo)
    salario = float(input("Digite o salário do empregado: "))
    while salario < 850.00 :
        salario = float(input("Digite o salário do empregado: "))
    if salario >= 3000 :
        reajuste = salario + (salario * 0.045)
        print("Salário reajustado: " ,reajuste)
    elif salario >= 2000 and salario < 3000 :
        reajuste = salario + (salario * 0.065)
        print("Salário reajustado: " ,reajuste)
        a = a + 1
    elif salario < 2000 :
        reajuste = salario + (salario * 0.085)
        print("Salário reajustado: " ,reajuste)
    if sexo == "M":
        m = m + 1
        r = r + reajuste
    elif sexo == "F":
        f = f + 1
        
    

salario_medio_M = r / m
print("\nQuantidade de empregados que receberam reajuste de 6,5%: " ,a)
print("Média do salário reajustado dos empregados do sexo masculino: " ,salario_medio_M)
print("Porcentagem de empregados do sexo feminino: " ,(f * 100) / qtd_empregados, "%")   




