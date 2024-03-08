while True:
    numero = int(input())

    if numero <= 0:
        break

    matriz = []
    for i in range(0, numero):
        matriz.append([])
        for j in range(0, numero):
            matriz[i].append(0) #APPEND VAI ADICIONAR

    if numero % 2 == 0:
        total = numero // 2
    else:
        total = 1 + numero // 2

    minimo = 0
    maximo = numero
    contador = 0

    for k in range(0, total):
        contador += 1
        for i in range(minimo, maximo):
            for j in range(minimo, maximo):
                matriz[i][j] = contador
        minimo += 1
        maximo -= 1

    for i in range(0, numero):
        for j in range(0, numero):
            matriz[i][j] = str(matriz[i][j]).rjust(3)
        impressao = ' '.join(matriz[i])
        print(impressao)
    print()
