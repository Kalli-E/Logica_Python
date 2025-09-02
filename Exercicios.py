produtos_loja = ["monitor", "mouse", "teclado", "placa de video", "headset"]
quantidade_produtos = [15, 30, 25, 20, 5]
precos = ["850.50", "85.00", "120.00", "1240.00", "250.00"]

estoque_loja = {"monitor":15, "mouse":30, "teclado":25, "placa de video":20, "headset": 5}
precos_produtos = {"monitor": 850.50, "mouse": 85.00, "teclado": 120.00, "placa de video": 1240.00, "headset": 250.00}

produto_procurado = input("Qual o produto que você deseja: ")
produto_procurado = produto_procurado.lower()

# print(estoque_loja)
# print(produtos_loja)
# print(quantidade_produtos)
# print(precos)

if produto_procurado in estoque_loja:
    print(f"Esse produto está disponível! Temos {estoque_loja[produto_procurado]} unidades disponíveis")

else:
    print(f"Este produto não está disponível em nosso estoque.")

    







