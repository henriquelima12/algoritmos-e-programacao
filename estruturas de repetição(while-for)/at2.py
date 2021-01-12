ct = 0
soma = 0
n = 0
pos = 0
neg = 0
par = 0
impar = 0
soma_par = 0


while ct < 5:
    entrada = int(input("Digite um número inteiro: "))
    if entrada > 0:
        pos = pos + entrada
    elif entrada < 0:
        neg = neg + 1

    if entrada % 2 == 0:
        par = par + 1
        soma_par = soma_par + entrada
    elif entrada % 2 == 1:
        impar = impar + 1
    
        
    soma = soma + entrada
    n = n + 1
    ct = ct + 1
    
media = soma / n
media_par = soma_par / par
porcent = (impar * 100) / n

print("Soma dos números digitados: " ,soma)
print("Qtd de números digitados: " ,n)
print("Média dos números digitados: %.2f" %media)
print("Soma dos números positivos: " ,pos)
print("Qtd de números negativos: " ,neg)
print("Média dos números pares: %.2f" %media_par)
print("Porcentagem de números ímpares: %.2f: " %porcent)
