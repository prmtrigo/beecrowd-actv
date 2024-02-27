segundos = int(input())

horas = segundos//3600
segundos %=3600
minutos = segundos//60
segundos %= 60

print("{:01d}:{:01d}:{:01d}".format(horas,minutos,segundos))