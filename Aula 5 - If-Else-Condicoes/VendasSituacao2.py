# Cenário 2

vendas = 1800
meta1 = 1300 # ganhar 10%
meta2 = 2000 # ganhar 13%

if vendas >= 2000:
    bonus = 0.13*vendas

elif vendas >= 1300:
    bonus = 0.1*vendas

else: 
#    if vendas >= 1300:
#       bonus = 0.1*vendas
#     else:
        bonus = 0

print ("Bonus: ", bonus)