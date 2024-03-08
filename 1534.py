while True:
    try:

        numero = int(input())

        if 3 <= numero <=70:

            matriz = [[3] * numero for i in range(numero)]

            for i in range (numero):
                for j in range (numero):
                    if i == j:
                        matriz[i][j] = 1
                    if i == numero - j - 1:
                        matriz[i][j] = 2
            
            for i in range (numero):
                for j in range (numero):
                    print(matriz[i][j], end="")
                print()

    except EOFError:
        break