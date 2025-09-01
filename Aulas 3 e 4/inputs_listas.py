#Input 
email = input("Escreva seu e-mail: ")
nome = input("Escreva seu nome: ")
print(nome, email)
print(f"{nome}, verifique seu e-mail: {email} para confirmação da sua conta.")
faturamento = float(input("Escreva o faturamento da empresa: "))
print(faturamento)
imposto = faturamento * 0.1
print(imposto)

#Listas
vendas = [100, 50, 15, 20, 30, 500, 150]
print(vendas)

#soma elementos da lista
total_vendas = sum(vendas)
print(total_vendas)

#tamanho da lista
quantidade_vendas = len(vendas)
print(quantidade_vendas)

# maximo e mínimo
print(max(vendas))
print(min(vendas))

# pegar uma posição da lista
print(vendas[-1])

# verificar um elemento da lista
lista_produtos = ["iphone", "airpod", "ipad", "macbook"]
print("airpod" in lista_produtos) #resultado boleano
produto_procurado = input("Pesquise o nome do produto: ")
produto_procurado = produto_procurado.lower()
print(produto_procurado in lista_produtos)

#adicionar um item na lista
lista_produtos.append("apple watch")
lista_produtos.remove("apple watch")
lista_produtos.pop(0)
print(lista_produtos)

#editar um item da lista
precos_produtos = [1000, 500, 2500, 1500]
precos_produtos[0] = precos_produtos[0] * 1.5
print(precos_produtos)

#contar quantas vezes um item aparece na lista
lista_produtos = ["iphone", "airpod", "ipad", "zulu", "iphone", "ipad", "iphone"]
print(lista_produtos.count("airpod"))

#ordenar uma lista
lista_produtos.sort() #ordem alfabética
lista_produtos.reverse() #ordem alfabética inversa
print(lista_produtos)

precos_produtos.sort() #ordem crescente
precos_produtos.reverse() #ordem decrescente
print(precos_produtos)









