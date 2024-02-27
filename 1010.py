codigo_produto_1, unidade_produto_1, preco_produto_1 = map(float, input().split())

codigo_produto_2, unidade_produto_2, preco_produto_2 = map(float, input().split())

quantidade = (unidade_produto_1 * preco_produto_1) + (unidade_produto_2 * preco_produto_2)

print("VALOR A PAGAR: R$ {:.2f}".format(quantidade))
