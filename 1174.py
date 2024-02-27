vetor = [0] * 100

for i in range(100):
    vetor[i] = float(input())

for i in range(100):
    if vetor[i] <= 10:
        print("A[{}] = {:.1f}".format(i, vetor[i]))
