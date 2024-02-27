vetor = [0] * 10

for i in range(10):
    vetor[i] = int(input())

for i in range(10):
    if vetor[i] <= 0:
        vetor[i] = 1

for i in range(10):
    print("X[{}] = {}".format(i, vetor[i]))

