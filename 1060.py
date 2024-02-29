#it is interesting to know how this range works in python

numeros_positivos = 0

for i in range(6):
    numero = float(input())
    if numero > 0:
        numeros_positivos +=1

print(numeros_positivos, "valores positivos")