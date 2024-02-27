import math

x_1, y_1 = map(float, input().split())
x_2,y_2 = map(float, input().split())

distancia_entre_pontos = math.sqrt((x_2 - x_1) ** 2 + (y_2 - y_1) ** 2)

print("{:.4f}".format(distancia_entre_pontos))