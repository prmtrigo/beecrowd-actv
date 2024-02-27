def calcular_fibonacci(n):
    if n <= 1:
        return n
    else:
        anterior, atual = 0, 1
        for _ in range(2, n + 1):
            anterior, atual = atual, anterior + atual
        return atual

quantidade_testes = int(input())

for _ in range(quantidade_testes):
    n = int(input())
    
    numero_fibonacci = calcular_fibonacci(n)

    print("Fib({}) = {}".format(n, numero_fibonacci))