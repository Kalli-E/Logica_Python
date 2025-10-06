vendas = int (input("Digite o valor das vendas: ")) # Neste caso, o input tem que ter o int para converter o valor em valor inteiro, para a realilzação do cálculo
vendas_empresa = 18000

meta_empresa = 18000
meta1 = 1300 #ganhar 10%
meta2 = 2000 #ganhar 13%
meta3 = 2500 #ganhar 15%

if vendas >= 2500 and vendas_empresa >= meta_empresa:
    bonus = 0.15 * vendas

elif vendas >= 2000 and vendas_empresa >= meta_empresa:
    bonus = 0.13 * vendas

elif vendas >= 1300 and vendas_empresa >= meta_empresa:
    bonus = 0.1 * vendas

else:
    bonus = 0

print ("Bonus: ", bonus)