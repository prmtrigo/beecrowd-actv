termo = int(input())

numero = []
for i in range(1000):
    numero.append(i % termo)


for i in range(1000):
    print("N[{}] = {}".format(i, numero[i]))