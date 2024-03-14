tamanho = int(input())
vetor = []

for i in range (tamanho):
    elemento = int(input())
    vetor.append(elemento)

valor_para_exclusao = int(input())

vetor.remove(valor_para_exclusao)

print(vetor)