import random
print("Escolha 0(zero) para pedra, 1(um) para papel e 2(dois) para tesoura.")
print("Para definir o vencedor segue-se a seguinte regra: ")
print("pedra ‘quebra’ a tesoura; tesoura ‘corta’ o papel e papel ‘embrulha’ a pedra. ")
print("Se ambas escolhem a mesma, há empate.")

user = int(input("Escolha entre 0(zero), 1(um) e 2(dois): "))
maquina = (random.randrange(0, 3))

print("Sua escolha: " ,user)
print("Escolha da máquina: " ,maquina)

if user == 0 and maquina == 1:
    print("Você escolheu pedra e a máquina escolheu papel, portanto você perdeu!")
elif user == 0 and maquina == 2:
    print("Você escolheu pedra e a máquina escolheu tesoura, portanto você ganhou!")
elif user == 1 and maquina == 0:
    print("Você escolheu papel e a máquina escolheu pedra, portanto você ganhou!")
elif user == 1 and maquina == 2:
    print("Você escolheu papel e a máquina escolheu tesoura, portanto você perdeu")
elif user == 2 and maquina == 0:
    print("Você escolheu tesoura e a máquina escolheu pedra, portanto você perdeu!")
elif user == 2 and maquina == 1:
    print("Você escolheu tesoura e a máquina escolheu papel, portanto você ganhou!")
elif user == 0 and maquina == 0:
    print("Você escolheu pedra e a máquina escolheu pedra, portanto deu empate!")
elif user == 1 and maquina == 1:
    print("Você escolheu papel e a máquina escolheu papel, portanto deu empate!")
elif user == 2 and maquina == 2:
    print("Você escolheu tesoura e a máquina escolheu tesoura, portanto deu empate!")
          
