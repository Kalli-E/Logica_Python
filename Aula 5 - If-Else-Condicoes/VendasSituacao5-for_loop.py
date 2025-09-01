#for i in range(10): # Repete o número de vezes de acordo com o inteiro (i), que é o parâmetro da declaração. O parâkmetro pode ser modificado conforme a necessidade
#   print("Loop do python")

#for item in lista_vendas:
#    print(item)

lista_vendas = [1000, 500, 800, 1500, 2000, 2300]
meta_vendas = int(input("Digite a meta mensal de vendas:"))

percentual_bonus = 0.1

for venda in lista_vendas:
    if venda >= meta_vendas:
        bonus = percentual_bonus*venda

    else:
        bonus = 0

    print("O bonus mensal é de: ", bonus)       
# OBS: Não esquecer de colocar o print dentro da estrutura de repetição (indentação), ou o código não funcionará.



