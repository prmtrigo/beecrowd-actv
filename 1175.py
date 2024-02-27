vetor = [0] * 20

for i in range(20):
    vetor[i] = int(input())

for i in range(10):
    vetor[i], vetor[19-i] = vetor[19-i], vetor[i]

for i in range(20):
    print("N[{}] = {}".format(i, vetor[i]))