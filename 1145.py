linhas, numeros = map(int, input().split())

for i in range (1, numeros +1):

    if (i % linhas == 0):
        print(i, end="\n")

    else:
        print(i, end=" ")