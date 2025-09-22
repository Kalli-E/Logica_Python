# Cenário 3
 # Neste caso, as comparações tem que ser da maior para a menor, ou o valor do bônus não será calculado corretamente
vendas = 2500
meta1 = 1300 # ganhar 10%
meta2 = 2000 # ganhar 13%
meta3 = 2500 # ganhar 15%

if vendas >= 2500:
    bonus = 0.15*vendas

elif vendas >=2000:
    bonus = 0.13*vendas

elif vendas >= 1300:
    bonus = 0.1*vendas

else: 
    bonus = 0

    print ("Bonus: ", bonus)
