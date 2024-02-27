primeira_nota = float(input())
segunda_nota = float(input())

peso_A = 3.5
peso_B = 7.5

media_ponderada = weighted_average = ((primeira_nota * peso_A) + (segunda_nota * peso_B)) / (peso_A + peso_B)

print("MEDIA = {:.5f}".format(media_ponderada))