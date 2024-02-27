numero = float(input())

vetor = [0] * 100
vetor[0] = numero

for i in range (1, 100):
    vetor[i] = vetor[i-1]/2


for i in range(100):
    print("N[{}] = {:.4f}".format(i, vetor[i]))