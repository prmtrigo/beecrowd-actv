casos_teste = int(input())

for i in  range(casos_teste):
    numeros = list(map(float, input().split()))

    media_ponderada = (numeros[0] * 2 + numeros[1] * 3 + numeros[2] * 5)/10

    print("{:.1f}".format(media_ponderada))