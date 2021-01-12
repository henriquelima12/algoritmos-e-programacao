a = 0
b = 1

f = int(input("Digite a quantidade de termos que você quer exibir: "))

for i in range(1, f, 1):
    if i == 1:
        print(b)
    c = a + b
    a = b
    b = c
    print(c)
