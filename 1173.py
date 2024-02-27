vetor = [0] * 10

numero = int(input())

vetor[0] = numero

for i in range(1,10):
    vetor[i] = vetor[i-1]*2

for i in range(10):
    print("N[{}] = {}".format(i, vetor[i]))