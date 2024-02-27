pares = []
impares = []

def imprimir_e_resetar(nome_lista, lista):
    for i, num in enumerate(lista):
        print("{}[{}] = {}".format(nome_lista, i, num))
    lista.clear()


for _ in range(15):
    num = int(input())
    if num % 2 == 0:
        pares.append(num)
        if len(pares) == 5:
            imprimir_e_resetar("par", pares)
    else:
        impares.append(num)
        if len(impares) == 5:
            imprimir_e_resetar("impar", impares)

imprimir_e_resetar("impar", impares)
imprimir_e_resetar("par", pares)
