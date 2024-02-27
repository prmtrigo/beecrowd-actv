codigo_produto,quantidade = map(int, input().split())

if (codigo_produto == 1):
    preco = 4.00
if (codigo_produto == 2):
    preco = 4.50
if (codigo_produto == 3):
    preco = 5.00
if (codigo_produto == 4):
    preco = 2.00
if (codigo_produto == 5):
    preco = 1.50

total = preco * quantidade

print("Total: R$ {:.2f}".format(total))