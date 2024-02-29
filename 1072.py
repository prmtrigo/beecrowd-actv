casos = int(input())

contador_dentro = 0
contador_fora = 0

for i in range(casos):
    numero = int(input())
    if 10 <= numero < 20:
        contador_dentro += 1
    else:
        contador_fora += 1

print(contador_dentro, "in")
print(contador_fora, "out")