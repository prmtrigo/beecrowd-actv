conta_alcool = 0
conta_gasolina = 0
conta_diesel = 0

while True:
    senha = int(input())

    if senha == 1:
        conta_alcool += 1
    elif  senha == 2:
        conta_gasolina += 1
    elif senha == 3:
        conta_diesel += 1
    elif senha == 4:
        break
    else:
        continue

print("MUITO OBRIGADO")
print("Alcool: {}".format(conta_alcool))
print("Gasolina: {}".format(conta_gasolina))
print("Diesel: {}".format(conta_diesel))
