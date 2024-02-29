#print(numeros_positivos, "valores positivos")
#print("{:.1f}".format(media_numeros_positivos))

numeros_positivos = 0
soma_positivos = 0

# Ler os 6 números e contar os positivos
for i in range(6):
    numero = float(input())
    if numero > 0:
        numeros_positivos += 1
        soma_positivos += numero

# Calcular a média dos números positivos
media_numeros_positivos = soma_positivos / numeros_positivos

print(numeros_positivos, "valores positivos")
print("{:.1f}".format(media_numeros_positivos))

