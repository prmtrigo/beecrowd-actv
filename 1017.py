tempo_horas = int(input())
velocidade_km_hora = int(input())
kilometro_litro = 12

distancia = tempo_horas * velocidade_km_hora
consumo_combustivel = distancia / kilometro_litro
print("{:.3f}".format(consumo_combustivel))
