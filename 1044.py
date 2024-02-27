numero_puro, suposto_multiplo = map(int, input().split())

if suposto_multiplo % numero_puro == 0 or numero_puro % suposto_multiplo == 0:
    print("Sao Multiplos")
else:
    print("Nao sao Multiplos")