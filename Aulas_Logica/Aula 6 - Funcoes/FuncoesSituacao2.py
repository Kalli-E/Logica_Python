# imposto
# aliquota 1 - IR - 0.2
# aliquota 2 - ISS - 0.15
# aliquota 3 - CSLL - 0.05

nova_lista_precos = [1900, 1000, 800, 3000]

# estrutura de repetição dentro de uma função. Uma função simplifica o código, diminuindo o tamanho de estruturas que precisarão ser instanciadas.
def calcula_imposto_total(preco):   
    if preco <= 2000:

        imposto_ir = 0.2* preco
    else:
        imposto_ir = 0.3* preco

    imposto_iss = 0.15*preco
    imposto_csll = 0.05* preco
    imposto_total = imposto_ir + imposto_iss + imposto_csll

    return imposto_total

for preco in nova_lista_precos:
    imposto_total = calcula_imposto_total(preco)
    print(f"Imposto total sobre o produto de R$ {preco}, é de R$ {imposto_total}")


# estrutura dse repetição sem função -> menos prático para lidar com grandes estruturas de dados
for preco in nova_lista_precos:

    if preco <= 2000:

        imposto_ir = 0.2* preco
    else:
        imposto_ir = 0.3* preco

    imposto_iss = 0.15*preco
    imposto_csll = 0.05* preco
    imposto_total = imposto_ir + imposto_iss + imposto_csll

    print(f"Imposto total sobre o produto de R$ {preco}, é de R$ {imposto_total}")

