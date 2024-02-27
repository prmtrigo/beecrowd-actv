A,B,C = map(float, input().split())

# para verificar se um triângulo pode ser feito
# um de seus lados deve ser maior que a diferença dos outros dois
# e também deve ser menor que a soma

if A + B > C and A + C > B and B + C > A:
    perimetro = A + B + C
    print("Perimetro = {:.1f}".format(perimetro))
else:
    area = ((A+B)*C)/2
    print("Area = {:.1f}".format(area))