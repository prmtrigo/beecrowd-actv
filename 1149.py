valores = input().split()

inicio = int(valores[0])
ultimo_valor = len(valores) -1
numero_ultimo_valor = int(valores[ultimo_valor])

contador = 0

for i in range(0, ultimo_valor+1):
    contador += inicio + i

print(contador)
