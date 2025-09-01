lista_produtos = ["airpod", "ipad", "iphone", "macbook"]
precos = ["2000", "9000", "13000", "20000"]

# dic_produtos = {"chave": valor, "chave2": valor2} -> sintaxe do dicionário
dic_produtos = {"airpod": 2000, "ipad": 9000, "iphone": 13000, "macbook": 20000}

#pegar um elemento
print(dic_produtos["airpod"])

#editar um elemeto
dic_produtos["iphone"] = dic_produtos["iphone"] * 0.8
print(dic_produtos)

#quantidade de itens do dicionario
print(len(dic_produtos))

#retirar um item do dicionario
dic_produtos.pop("airpod")
print(dic_produtos)

#adicionar um item no dicionário
dic_produtos["apple watch"] = 2500
print(dic_produtos)

#verificar se um item existe no dicionário
if "iphone" in dic_produtos:
    print("Há o produto desejado no estoque")
else:
    print("Não há o produto desejado no estoque.")

#Verificar se um valor existe no dicionário
if 9000 in dic_produtos.values():
    print("existe")

else:
    print("não existe")

    #print("Há", len(dic_produtos.values) "produtos com esse valor no estoque.")

# Cadastrar o novo produto (caso ele não exista)
# Caso o produto exista, ele edita o produto

nome_produto = input("nome do produto: ")
preco_produto = input("Preço do produto: ")

nome_produto = nome_produto.lower() #todos os nomes terão letras minúsculas no início, independente de como foram cadastradas
preco_produto = float(preco_produto)

dic_produtos[nome_produto] = preco_produto
print(dic_produtos)

produto = "airpod"

novo_preco = dic_produtos[produto]*1.1
print(novo_preco)

dic_produtos[produto] = novo_preco
print(dic_produtos)

# Além disso, o produto tem que atualizar o preço de todos os produtos para os valores em 10% a mais do que o preço original

for produto in dic_produtos:
    novo_preco = dic_produtos[produto]*1.1
    dic_produtos[produto] = novo_preco

print(dic_produtos)