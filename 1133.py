primeiro_numero = int(input())
ultimo_numero = int(input())

if primeiro_numero > ultimo_numero:
    primeiro_numero, ultimo_numero = ultimo_numero, primeiro_numero

for i in range(primeiro_numero + 1, ultimo_numero):
    if i % 5 == 2 or i % 5 == 3:
        print(i)