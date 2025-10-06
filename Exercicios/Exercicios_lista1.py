# Exercício: Sistema de controle e estoque

produtos_loja = ["monitor", "mouse", "teclado", "placa de video", "headset"]
quantidade_produtos = [15, 30, 25, 20, 5]
precos = ["850.50", "85.00", "120.00", "1240.00", "250.00"]

estoque_loja = {"monitor":15, "mouse":30, "teclado":25, "placa de video":20, "headset": 5}
precos_produtos = {"monitor": 850.50, "mouse": 85.00, "teclado": 120.00, "placa de video": 1240.00, "headset": 250.00}

#############################################################

produto_procurado = input("Qual o produto que você deseja comprar: ").lower()
# produto_procurado = produto_procurado.lower()

if produto_procurado in estoque_loja:
    print(f"Esse produto está disponível! Temos {estoque_loja[produto_procurado]} unidades de '{produto_procurado}' disponíveis")
       
    continuar_compra = input("Deseja continuar com a compra? [Sim/Não]: ").lower()
    
    while continuar_compra != "sim" and continuar_compra != "não":
        print("Opção inválida, digite uma opção válida.")
        continuar_compra = input("Deseja continuar com a compra? [Sim/Não]: ").lower()
    
    if continuar_compra == "não":
        print("\nCompra cancelada.")
        exit()
        
    elif continuar_compra == "sim":
        quantidade_desejada = int(input("Digite a quantidade desejada: "))
            
        if quantidade_desejada <= estoque_loja[produto_procurado]:
            estoque_loja[produto_procurado] -= quantidade_desejada
            valor_total = quantidade_desejada * precos_produtos[produto_procurado]
            print(f"\nVenda de {quantidade_desejada} unidades de '{produto_procurado}' realizada com sucesso. Total: R$ {valor_total:.2f}")
            print(f"\nEstoque atualizado: {estoque_loja[produto_procurado]} unidades restantes de '{produto_procurado}'.")

        elif quantidade_desejada > estoque_loja[produto_procurado]:
            print("\nNão há estoque suficiente deste produto.")

else:
    print(f"\nEste produto não está disponível em nosso estoque.")

#############################################################

print("\nCálculo de impostos:")

def calcular_imposto(preco):
    imposto = 0.15 * preco
    return imposto

imposto_total = calcular_imposto(valor_total)
imposto_somado = valor_total + imposto_total
print(f"\nA venda de '{produto_procurado}' teve o acréscimo de 15% de seu valor. O total do acréscimo foi de R$ {imposto_total:.2f}, totalizando R$ {imposto_somado:.2f}.")

#############################################################

print("\nEstoque e orçamento final:")

for produto, quantidade in estoque_loja.items():
    print ("Estoque atualizado:")
    print(f"Produto: {produto}, Estoque atual: {quantidade} unidades")

lucro_total = valor_total - imposto_total
print(f"\nO lucro total com a venda realizada foi de R$ {lucro_total:.2f}.")

#############################################################




