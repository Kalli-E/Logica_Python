produtos_loja = ["monitor", "mouse", "teclado", "placa de video", "headset"]
quantidade_produtos = [15, 30, 25, 20, 5]
precos = ["850.50", "85.00", "120.00", "1240.00", "250.00"]

estoque_loja = {"monitor":15, "mouse":30, "teclado":25, "placa de video":20, "headset": 5}
precos_produtos = {"monitor": 850.50, "mouse": 85.00, "teclado": 120.00, "placa de video": 1240.00, "headset": 250.00}

produto_procurado = input("Qual o produto que você deseja: ")
produto_procurado = produto_procurado.lower()

# Teste 1
# print(estoque_loja)
# print(produtos_loja)
# print(quantidade_produtos)
# print(precos)

if produto_procurado in estoque_loja:
    print(f"Esse produto está disponível! Temos {estoque_loja[produto_procurado]} unidades de '{produto_procurado}' disponíveis")

else:
    print(f"Este produto não está disponível em nosso estoque.")

    
#▪ Se o produto estiver em estoque:
#▪ Pergunte ao usuário a quantidade desejada.
#▪ Verifique se a quantidade solicitada é menor ou igual à quantidade em estoque.
#▪ Se for, atualize o estoque subtraindo a quantidade vendida.
#▪ Calcule o valor total da venda (quantidade * preço).
#▪ Imprima uma mensagem de sucesso, como "Venda de X unidades de Y realizada com sucesso. Total: R$ Z".
#▪ Se não houver quantidade suficiente:
#▪ Imprima uma mensagem informando que não há estoque suficiente.
#▪ Se o produto não existir:
#▪ Imprima uma mensagem de erro, como "Produto não encontrado.".






