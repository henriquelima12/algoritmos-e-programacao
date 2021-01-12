import random

num_pessoa = int(input("Escolha um número entre 1 e 10: "))
escolha = int(input("Escolha 0(zero) para par e 1(um) para ímpar: "))
num_maquina = (random.randrange(0, 11))
print("Número que você escolheu: " ,num_pessoa)
print("Número que a máquina escolheu: " ,num_maquina)

if (num_pessoa + num_maquina) % 2 ==0 and escolha == 0:
    print("Você escolheu par e a soma dos números é par. Portanto você ganhou!")
elif (num_pessoa + num_maquina) % 2 ==0 and escolha == 1:
    print("Você escolheu ímpar e a soma dos números é par. Portanto você perdeu!")
elif (num_pessoa + num_maquina) % 2 == 1 and escolha == 1:
    print("Você escolheu ímpar e a soma dos números é ímpar. Portanto você ganhou!")
elif (num_pessoa + num_maquina) % 2 ==1 and escolha == 0:
    print("Você escolheu par e a soma dos números é ímpar. Portanto você perdeu!")







