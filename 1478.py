while True:

    numero = int(input())

    if numero == 0:
        break

    matriz_resultado = []

    for i in range (1, numero+1):
        matriz_temporaria = []
        referencia = i
        for j in range (numero):
            matriz_temporaria.append(abs(referencia))
            if(referencia == 1):
                referencia -=3 
            else:
                referencia -=1
        matriz_resultado.append(matriz_temporaria)

    for i in range(numero):
        tx = ''
        for j in range(numero):
            tx += " %3d" %matriz_resultado[i][j]
        print(tx[1:])
    print("")
