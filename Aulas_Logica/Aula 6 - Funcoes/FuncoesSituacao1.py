# imposto
# aliquota 1 - IR - 0.2
# aliquota 2 - ISS - 0.15
# aliquota 3 - CSLL - 0.05

lista_precos = [1500, 1000, 800, 3000]

for preco in lista_precos:
    
    imposto_ir = 0.2* preco
    imposto_iss = 0.15* preco
    imposto_csll = 0.05* preco
    imposto_total = imposto_ir + imposto_iss + imposto_csll

    print(f"Imposto total sobre o produto de R$ {preco}, é de R$ {imposto_total}")

