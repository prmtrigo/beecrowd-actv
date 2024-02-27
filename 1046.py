hora_comeco,hora_fim = map(int, input().split())

duracao = hora_fim - hora_comeco

if duracao <= 0:
    duracao += 24

print("O JOGO DUROU {} HORA(S)".format(duracao))