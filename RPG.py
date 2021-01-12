import random

m = 100
a = 1
b = 1
c = 1
d = 1
e = 1
f = 1
print(" MEMBROS DO GRUPO: ")
print(" HENRIQUE LIMA ARAÚJO, TIA: 32091702")
print(" LUCAS LIMA XAVIER DOS SANTOS, TIA: 32020724 \n")
print(" Você está perdido em uma floresta com apenas 100 moedas no seu bolso, \n precisando encontrar a saída. No entanto, você enfrentará vários perigos para  \n conseguir encontrar a saída e vencer o jogo. \n")
print(" Para derrotar todos os perigos e encontrar a saída, você precisa responder  \n corretamente todas as perguntas. \n Cada pergunta respondida corretamente acumulará mais moedas para o jogador,  \n além de deixa-lo mais perto do final do percurso entre a floresta. ")
print(" Porém, se alguma pergunta for respondida de maneira errada, o usuário perde \n todas as moedas e automaticamente perde o jogo.")
print(" Após derrotar todos os perigos da floresta, o usuário precisará jogar os dados \n e acertar os números para conseguir achar o caminho correto, pois cada jogada \n errada resultará na perda de moedas")
print(" Ao final do jogo, a sua pontuação se dará pelo número de moedas que foram \n acumuladas durante todo o percurso. Seu desempenho será avaliado  \n desde iniciante até máster. \n")


print("Você deu de cara com um Leão feroz. Para conseguir derrotá-lo e avançar, \n responda a seguinte pergunta: ")
quest1 = input("A qual grupo de animais o leão pertence? \n a)Mamíferos \n b)Aves \n c)Anfíbios \n d)Répteis \n ")

while a == 1:
    if quest1 == "a":
        print("Acertou. Você ganhou 100! Prossiga para a próxima fase.")
        m = m + 100
    else:
        print("Game Over! Infelizmente você não conseguiu derrotar o leão e perdeu todas as moedas.")
        m = m - 100
    a = a + 1

print("Moedas: " ,m)

if m == 0:
    print("Jogo acabou!")
else:
    print("Dessa vez você encontrou com um Urso-Pardo. Para conseguir derrotá-lo e avançar, responda a seguinte pergunta: ")
    quest2 = input(" Quantos anos, em média, vive um Urso-Pardo? \n a)De 10 a 15 anos \n b)De 15 a 20 anos \n c)De 25 a 30 anos \n d)De 35 a 40 anos \n ")

    while b == 1:
        if quest2 == "c":
            print("Acertou. Você ganhou mais 100! Prossiga para a próxima fase.")
            m = m + 100
        else:
            print("Game Over! Infelizmente você não conseguiu derrotar o Urso-Pardo e perdeu todas as moedas.")
            m = m - 200
        b = b+1

    print("Moedas: " ,m)

    if m == 0:
        print("Jogo acabou!")
    else:
        print("Você está indo bem! No entanto, agora você deu de cara com com uma lagoa \n cheia de Crocodilos. Para conseguir derrotá-los e avançar, responda a seguinte pergunta: ")
        quest3 = input("Quanto tempo os Crocodilos podem ficar sem comer? \n a)De 6 a 10 meses \n b)De 1 a 2 anos \n c)De 2 a 2 anos e meio \n d)Até 3 anos \n ")

        while c == 1:
            if quest3 == "d":
                print("Acertou. Você ganhou mais 100! Prossiga para a próxima fase!")
                m = m + 100
            else:
                print("Game Over! Infelizmente você não conseguiu passar pela lagoa de Crocodilos e perdeu todas as moedas!")
                m = m - 300
            c = c+1

        print("Dinheiro: " ,m)

        if m == 0:
            print("Jogo acabou!")
        else:
            print("Boa! Você está chegando quase lá. Agora você precisa destruir uma tropa de soldados. Para conseguir derrotá-los e avançar, responda a seguinte pergunta: ")
            quest4 = input("Que dia é considerado como o Dia do Soldado? \n a)12 de Fevereiro \n b)30 de Abril \n c)25 de Agosto \n d)8 de Outubro \n ")

            while d == 1:
                if quest4 == "c":
                    print("Acertou. Você ganhou mais 100! Prossiga para a próxima fase!")
                    m = m + 100
                else:
                    print("Game Over! Infelizmente você não conseguiu passar pela tropa de soldados e perdeu todas as moedas!")
                    m = m - 400
                d = d+1
                
            print("Moedas: " ,m)

            
            if m == 0:
                print("Jogo acabou!")
            else:
                print("É isso aí, você está no caminho certo! Agora você precisa passar pelo trecho de areia movediça. Para isso, responda a seguinte pergunta: ")
                quest5 = input("Qual das alternativas consta apenas maravilhas do mundo? \n a)Cristo Redentor, Centro Histórico de Ouro Preto \n b)Pirâmides do Egito, Coliseu de Roma \n c)Taj Mahal, Pirâmide do Sol  \n d)Machu Picchu, Colosso de Rodes \n ")

                while e == 1:
                    if quest5 == "b":
                        print("Acertou. Você ganhou mais 100! Prossiga para a próxima fase!")
                        m = m + 100
                    else:
                        print("Game Over! Infelizmente você não conseguiu passar pela areia movediça e perdeu todas as moedas!")
                        m = m - 500
                    e = e+1
                
                print("Moedas: " ,m)

                if m == 0:
                    print("Jogo acabou!")
                else:
                    print("Você está quase lá! Para conseguir vencer todos os obstáculos, você precisa derrotarar pelo grupo de Índios da floresta. Para isso, responda a seguinte pergunta: ")
                    quest6 = input("Quem é considerado como o feiticeiro das tribos 6? \n a)Cacique \n b)Tupi \n c)Curumim \n d)Pajé \n ")

                    while f == 1:
                        if quest6 == "d":
                            print("Acertou. Você ganhou mais 100! Prossiga para a próxima fase!")
                            m = m + 100
                        else:
                            print("Game Over! Infelizmente você não conseguiu passar pelo grupo de Índios e perdeu todas as moedas!")
                            m = m - 600
                        f = f+1
                
                    print("Moedas: " ,m)
                    

if m == 0:
    print("Fim de Jogo! Você não conseguiu moedas suficente para passar de fase!")
else:
    print(" Parabéns, você passou para a próxima fase!")
    print(" Você conseguiu superar todos os obstáculos. Parabéns! A partir de agora, você \n vai precisar de muita sorte para se dar bem no jogo de dados e achar o caminho \n certo para chegar ao final da floresta")

    dados = int(input(" Acerte o número dos dados. Digite um número entre 2 e 12: "))
    while dados <2 or dados >12 :
        dados = int(input(" Acerte o número dos dados. Digite um número entre 2 e 12: "))
        
    comp = (random.randrange(1, 7))
    print ("Dado 1: " ,comp)
    comp2 = (random.randrange(1, 7))
    print ("Dado 2: " ,comp2)
    soma = comp + comp2
    print("A soma dos dados é: " ,soma)

    if dados == soma:
        print("Você conseguiu. Chegou ao final da floresta. Você é o grande vencedor!")
    elif dados != soma:
        print("Jogue novamente os dados")
        m = m - 100
        
        while m > 0 and dados != soma:
            print("Você perdeu 100 moedas. Suas moedas: " ,m)
            
            dados = int(input(" Acerte o número dos dados. Digite um número entre 2 e 12: "))
            while dados <2 or dados >12 :
                dados = int(input(" Acerte o número dos dados. Digite um número entre 2 e 12: "))
            
            comp = (random.randrange(1, 7))
            print ("Dado 1: " ,comp)
            comp2 = (random.randrange(1, 7))
            print ("Dado 2: " ,comp2)
            soma = comp + comp2
            print("A soma dos dados é: " ,soma)

            if dados != soma:
                m = m - 100

            if dados == soma:
                 print("Você conseguiu chegar ao final da floresta. Você é o grande vencedor!")
                
            if m == 0:
                print("Moedas: " ,m)
                print("Game Over! Infelizmente você não conseguiu achar o caminho certo para chegar ao final e perdeu todas as moedas!")
                print("Fim de jogo")



    print("Sua pontuação final em moedas é: " ,m)

if m >= 0 and m < 300:
    print("Seu nível é Iniciante")
elif m == 300:
    print("Seu nível é Amador")
elif m == 400:
    print("Seu nível é Regular")
elif m == 500:
    print("Seu nível é Profissional")
elif m == 600: 
    print("Seu nível é Avançado")
elif m == 700:
    print("Seu nível é Master")


            
                
        
   
        
        
        

    
    
        


         
    
         
    




        
       
       



