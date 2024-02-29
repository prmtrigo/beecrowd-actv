contador_par = 0
contador_impar = 0
contador_positivo = 0
contador_negativo = 0

for i in range(5):
    numero = int(input())
    if numero % 2 == 0:
        contador_par += 1
    else:
        contador_impar += 1
    
    if numero < 0:
        contador_negativo += 1
    elif numero > 0:
        contador_positivo += 1

print(contador_par, "valor(es) par(es)")
print(contador_impar, "valor(es) impar(es)")
print(contador_positivo, "valor(es) positivo(s)")
print(contador_negativo, "valor(es) negativo(s)")