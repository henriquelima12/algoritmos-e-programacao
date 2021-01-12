#Autor: Henrique Lima
#Data: 25/03/2020
#Receber a nota do aluno, calcular sua média e mostrar se o aluno está aprovado ou reprovado.

nota_1 = float(input("Digite a primeira nota: "))
nota_2 = float(input("Digite a segunda nota: "))
nota_3 = float(input("Digite a terceira nota: "))
media = ((nota_1 * 2) + (nota_2 * 3) + (nota_3 * 5)) / 10

if media >= 6:
    print("Aluno aprovado com média: %.2f" %media)
else:
    print("Aluno reprovado com média: %.2f" %media)
