gabarito = ['d', 'b', 'c', 'a', 'c', 'e', 'c', 'd', 'a', 'b']
respostas = []

def instrucao():
    print("MEMBROS DO GRUPO: ")
    print("FELIPE DANTAS TAVARES, TIA: 32080549")
    print("HENRIQUE LIMA ARAÚJO, TIA: 32091702")
    print("LUCAS LIMA XAVIER DOS SANTOS, TIA: 32020724 \n")
    print("Você está jogando o nosso quiz de matemática!!!")
    print("Responda 10 perguntas relacionadas com a disciplina de matemática, envolvendo assuntos como matemática básica, tabuada e equações. ")
    print("As perguntas são constituídas de 5 alternativas, sendo apenas uma a alternativa correta. ")
    print("Cada pergunta vale 10 pontos, e, ao responder corretamente, o usuário irá acumular os pontos. ")
    print("Dessa forma, ao final do quiz, de acordo com a quantidade de pontos acumulados, o usuário receberá uma classificação de acordo com o seu desempenho. \n ")

def primeira():
    um = 0
    print ('Questão 1) - NÍVEL FÁCIL - Assinale a alternativa que mostra corretamente o total de números primos que existem entre os números 1, 7, 9, 11, 13, 29, 33:')
    print ('a) 2')
    print ('b) 8')
    print ('c) 6')
    print ('d) 4') 
    print ('e) 1')
    q1 = input('Escolha a alternativa correta: ')
    while q1 != 'a' and q1 != 'b' and q1 != 'c' and q1 != 'd' and q1 != 'e':
        q1 = input('Opção inválida! Escolha a alternativa correta: ')
    respostas.append(q1)

    if q1 == 'd':
        um = um + 1
        print("Resposta Correta\n")
    else:
        print("Resposta Errada")
        print("Justificativa: Numero primo é aquele que tem apenas 2 divisores(1 e ele mesmo), ou seja, letra d, 4. \n")

    return um

def segunda():
    dois = 0
    print('Questão 2)) - NÍVEL FÁCIL - A fração que corresponde ao número 0,56 é: ')
    print('a) 7/100') 
    print('b) 14/25')
    print('c) 28/25')
    print('d) 28/100')
    print('e) 14/50')
    q2 = input('Escolha a alternativa correta: ')
    while q2 != 'a' and q2 != 'b' and q2 != 'c' and q2 != 'd' and q2 != 'e':
        q2 = input('Opção inválida! Escolha a alternativa correta: ')
    respostas.append(q2)

    if q2 == 'b':
        dois = dois + 1
        print("Resposta Correta\n")
    else:
        print("Resposta Errada")
        print("Justificativa: 0,56 = 56/100; 56/100:(2/2) = 28/50; 28/50:(2/2) = 14/25. \n")
        
    return dois

def terceira():
    tres = 0
    print('Questão 3)- NÍVEL MÉDIO - Um clube promoveu um show de música popular brasileira ao qual compareceram 200 pessoas entre sócios e não sócios.')
    print('No total, o valor arrecadado foi de R$ 1 400,00 e todas as pessoas pagaram ingresso.')
    print('Sabendo-se que o preço do ingresso foi de R$ 10,00 e que cada sócio pagou metade desse valor, o número de sócios presentes foi:')
    print('a) 80')
    print('b) 100') 
    print('c) 120')
    print('d) 140')
    print('e) 160')
    q3 = input('Escolha a alternativa correta: ')
    while q3 != 'a' and q3 != 'b' and q3 != 'c' and q3 != 'd' and q3 != 'e':
        q3 = input('Opção inválida! Escolha a alternativa correta: ')
    respostas.append(q3)

    if q3 == 'c':
        tres = tres + 1
        print("Resposta Correta\n")
    else:
        print("Resposta Errada")
        print("Justificativa: Sócios: x / não sócios: y; x + y = 200(equação a); 5x + 10y = 1400(equação b); De (a): y = 200 - x;")
        print("Substituindo em (b): 5x + 10y = 1400; 5x + 10(200 - x) = 1400")
        print("5x + 2000 - 10x = 1400; -5x = -600; x = 120; Logo y = 80. \n")
              
    return tres

def quarta():
    quatro = 0
    print('Questão 4) - NÍVEL FÁCIL - Sabe-se que o preço a ser pago por uma corrida de táxi inclui uma parcela fixa, que é denominada bandeirada, e uma parcela variável,')
    print('que é função da distância percorrida.')
    print('Se o preço da bandeirada é R$4,60 e o quilômetro rodado é R$0,96, qual a distância percorrida por um passageiro que pagou R$19,00?')
    print('a) 15 km')
    print('b) 16 km')
    print('c) 17 km')
    print('d) 18 km')
    print('e) 19 km')
    q4 = input('Escolha a alternativa correta: ')
    while q4 != 'a' and q4 != 'b' and q4 != 'c' and q4 != 'd' and q4 != 'e': 
        q4 = input('Opção inválida! Escolha a alternativa correta: ')
    respostas.append(q4)

    if q4 == 'a':
        quatro = quatro + 1
        print("Resposta Correta\n")
    else:
        print("Resposta Errada")
        print("Justificativa: f(x) = 4,60 + 0,96x; Se um passageiro pagou R$ 19,00, temos: 19 = 4,60 + 0,96x; 0,96x = 19 - 4,60; 0,96x = 14,40; x= 14,40/0,96; x= 15. \n")
        
    return quatro
        
def quinta():
    cinco = 0
    print('Questão 5) - NÍVEL MÉDIO - A soma de três números inteiros consecutivos é 60. Qual é o produto entre esses três números?')
    print('a) 19, 20 e 21')
    print('b) 19')
    print('c) 7980')
    print('d) 6859')
    print('e) 44')
    q5 = input('Escolha a alternativa correta: ')
    while q5 != 'a' and q5 != 'b' and q5 != 'c' and q5 != 'd' and q5 != 'e':
        q5 = input('Opção inválida! Escolha a alternativa correta: ')
    respostas.append(q5)

    if q5 == 'c':
        cinco = cinco + 1
        print("Resposta Correta\n")
    else:
        print("Resposta Errada")
        print("Justificativa: Temos um número x somado com dois números consecutivos, resultando em 60: x + (x + 1) + (x + 2) = 60; 3x = 60 - 3; 3x = 57; x =  19;")
        print("Logo os números são: 19,  21 e 21; 19 x 20 x 21 = 7980. \n")

    return cinco
        
def sexta():
    seis = 0
    print ('Questão 6) - NÍVEL FÁCIL - A soma de um número com seu quíntuplo é igual ao dobro desse mesmo número somado com 40. Que número é esse?')
    print('a) 6')
    print('b) 7')
    print('c) 8')
    print('d) 9')
    print('e) 10')
    q6 = input('Escolha a alternativa correta: ')
    while q6 != 'a' and q6 != 'b' and q6 != 'c' and q6 != 'd' and q6 != 'e':
        q6 = input('Opção inválida! Escolha a alternativa correta: ')
    respostas.append(q6)

    if q6 == 'e':
        seis = seis + 1
        print("Resposta Correta\n")
    else:
        print("Resposta Errada")
        print("Justificativa: Temos um número x, somado com seu quíntuplo, resultando no dobro o número somado com 40: x + 5x = 2x + 40; x + 5x – 2x = 40;")
        print("6x – 2x = 40; 4x = 40; x = 40/4; x = 10. \n")

    return seis

def setima():
    sete = 0
    print('Questão 7) - NÍVEL DIFÍCIL - Uma máquina fotográfica custava R$ 500,00. No dia dos pais, numa promoção, foi vendida com um desconto de 10% e,')
    print('logo depois, em cima do novo preço sofreu um aumento de 10%. O seu preço atual, em reais, é: ')
    print('a) 450,00')
    print('b) 475,00')
    print('c) 495,00')
    print('d) 515,00')
    print('e) 500,00')
    q7 = input('Escolha a alternativa correta: ')
    while q7 != 'a' and q7 != 'b' and q7 != 'c' and q7 != 'd' and q7 != 'e':
        q7 = input('Opção inválida! Escolha a alternativa correta: ')
    respostas.append(q7)

    if q7 == 'c':
        sete = sete + 1
        print("Resposta Correta\n")
    else:
        print("Resposta Errada")
        print("Justificativa: 10% = 0,1; 500 x 0,1 = 50 (valor do desconto); 500 - 50 = 450;450 x 0,1 = 45 (valor do aumento); 450 + 45 = 495,00. \n")
        
    return sete

def oitava():
    oito = 0
    print('Questão 8) - NÍVEL DIFÍCIL - Para ligar a energia elétrica em seu apartamento, Felipe contratou um eletricista que mediu a distância do poste da rede elétrica até seu imóvel.')
    print('Essa distância é representada pela expressão ( 2√50 + 6√12 )m.')
    print('Para fazer a ligação, será necessário o dobro da medida fornecida pela expressão, já que serão necessários dois fios.')
    print('Nessas condições, a quantidade aproximada de fio, em metros, que Felipe terá que comprar é de')
    print('a) 18,48')
    print('b) 32,00')
    print('c) 38,00')
    print('d) 34,86')
    print('e) 36,00')
    q8 = input('Escolha a alternativa correta: ')
    while q8 != 'a' and q8 != 'b' and q8 != 'c' and q8 != 'd' and q8 != 'e':
        q8 = input('Opção inválida! Escolha a alternativa correta: ')
    respostas.append(q8)
        
    if q8 == 'd':
        oito = oito + 1
        print("Resposta Correta\n")
    else:
        print("Resposta Errada")
        print("Justificativa: 2(10√2 + 12√3) = 20√2 + 24√3 = 20.1,41 + 24.1,73 = 28,2 + 41,52 = 69,72m /2 = 34,86. \n")

    return oito
        
def nona():
    nove = 0
    print('Questão 9) - NÍVEL MÉDIO - Em uma escola com 1.200 alunos foi realizada uma pesquisa sobre o conhecimento desses em duas línguas estrangeiras: inglês e espanhol.')
    print('Nessa pesquisa constatou-se que 600 alunos falam inglês, 500 falam espanhol e 300 não falam qualquer um desses idiomas.')
    print('Escolhendo-se um aluno dessa escola ao acaso e sabendo-se que ele não fala inglês, qual a probabilidade de que esse aluno fale espanhol?')
    print('a) 1/2')
    print('b) 5/8')
    print('c) 1/4')
    print('d) 5/6')
    print('e) 5/14')
    q9 = input('Escolha a alternativa correta: ')
    while q9 != 'a' and q9 != 'b' and q9 != 'c' and q9 != 'd' and q9 != 'e':
        q9 = input('Opção inválida! Escolha a alternativa correta: ')
    respostas.append(q9)
        
    if q9 == 'a':
        nove = nove + 1
        print("Resposta Correta\n")
    else:
        print("Resposta Errada")
        print("Justificativa: Alunos que falam inglês e espanhol: (600-x) + x + (500-x) + 300 = 1200; -x = 1200 – 600 – 500 -300; x= 200;")
        print("Os alunos que não falam inglês somam: 300+300=600")
        print("A probabilidade de um aluno que não fala inglês falar espanhol é: 300/600 = 1/2. \n")

    return nove

def decima():
    dez = 0
    print('Questão 10)  - NÍVEL DIFÍCIL - Jogar baralho é uma atividade que estimula o raciocínio. Um jogo tradicional é a Paciência, que utiliza 52 cartas. ')
    print('Inicialmente, são formadas sete colunas com as cartas. A primeira coluna possui uma carta, a segunda possui duas cartas, a terceira tem três cartas, a quarta tem quatro cartas, ')
    print('e assim sucessivamente até a sétima coluna, a qual tem sete cartas, e o que sobra forma o monte, que são as cartas não utilizadas nas colunas.')
    print('A quantidade de cartas que forma o monte é: ')
    print("a) 21.")
    print("b) 24.")
    print("c) 26.")
    print("d) 28.")
    print("e) 31.")
    q10 = input('Escolha a alternativa correta: ')
    while q10 != 'a' and q10 != 'b' and q10 != 'c' and q10 != 'd' and q10 != 'e':
        q10 = input('Opção inválida! Escolha a alternativa correta: ')
    respostas.append(q10)
        
    if q10 == 'b':
        dez = dez + 1
        print("Resposta Correta")
        print("Quiz finalizado!\n")
    else:
        print("Resposta Errada")
        print("Justificativa: Progressão aritmética: 1, 2, 3, 4, 5, 6, 7. Soma dos termos de uma PA = (a1 + an) * a / 2;")
        print("a1 = 1; an = 7; n = 7; Sn = 8.7/2; Sn = 4.7; Sn = 28; Total de cartas(52) - Soma da quantidade de cartas(28) = 24 cartas no monte.")
        print("Quiz finalizado!\n")

    return dez
        
def mostrar():
    print("Suas respostas:")
    for a in range(10):
        print(respostas[a], ' ' ,end='')
    print("\n")
    print("Gabarito do quiz:")   
    for i in range(10):
        print(gabarito[i], ' ' ,end='')
    print("\n")

def classificacao(c):
    print("Quantidade de respostas certas: " ,c)

    if c < 6:
        print("Seu nível é Iniciante")
    elif c == 6:
        print("Seu nível é Amador")
    elif c == 7:
        print("Seu nível é Regular")
    elif c == 8:
        print("Seu nível é Profissional")
    elif c == 9: 
        print("Seu nível é Avançado")
    elif c == 10:
        print("Seu nível é Master")

def main():
    instrucao()
    a = primeira()
    b = segunda()
    c = terceira()
    d = quarta()
    e = quinta()
    f = sexta()
    g = setima()
    h = oitava()
    i = nona()
    j = decima()
    classif = a + b + c + d + e + f + g + h + i + j
    mostrar()
    classificacao(classif)

main()
    

