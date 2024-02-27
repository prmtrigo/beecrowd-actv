primeira_nota = float(input())
segunda_nota = float(input())
terceira_nota = float(input())

peso_primeiro = 2
peso_segundo = 3
peso_terceiro = 5

media_ponderada = (((primeira_nota * peso_primeiro) + (segunda_nota * peso_segundo) + (terceira_nota * peso_terceiro))/ (peso_terceiro + peso_primeiro + peso_segundo))

print("MEDIA =", "{:.1f}".format(media_ponderada))

