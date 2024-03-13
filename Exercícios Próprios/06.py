def produto_com_desconto(preco_cheio, percentual_desconto):
    preco_total = preco_cheio - (preco_cheio * (percentual_desconto/100))

    return preco_total

preco_cheio = int(input())
percentual_desconto = int(input())
print(produto_com_desconto(preco_cheio, percentual_desconto))