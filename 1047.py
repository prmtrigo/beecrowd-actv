hora_inicio, minuto_inicio, hora_fim, minuto_fim = map(int, input().split())

verdadeiro_inicio = hora_inicio * 60 + minuto_inicio
verdadeiro_fim = hora_fim * 60 + minuto_fim

duracao_minuto = verdadeiro_fim - verdadeiro_inicio

if duracao_minuto <= 0:
    duracao_minuto += 24*60

duracao_hora = duracao_minuto//60
duracao_minuto %=60

print("O JOGO DUROU {} HORA(S) E {} MINUTO(S)".format(duracao_hora, duracao_minuto))