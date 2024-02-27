eixo_x,eixo_y = map(float, input().split())

if eixo_x == 0 and eixo_y == 0:
    print("Origem")
elif eixo_x == 0:
    print("Eixo Y")
elif eixo_y == 0:
    print("Eixo X")
elif eixo_x > 0:
    if eixo_y > 0:
        print("Q1")
    else:
        print("Q4")
else: # eixo_x < 0
    if eixo_y > 0:
        print("Q2")
    else:
        print("Q3")