faturamento = 1500 # variável tipo int
custo = 750.25 # variável tipo float (casa decimal)
novas_vendas = 100
imposto = faturamento * 0.1
lucro = faturamento - custo - imposto
margem_lucro = lucro / faturamento
faturamento = faturamento + novas_vendas
imposto = faturamento * 0.14

nome = 'Augusto'#variável tipo string (texto)
#teve_lucro = True #variável tipo bolean
#email = 'meuemail@email.com' #tipo string (texto)

print("Meu nome é", nome)
print("O Faturamento foi de", faturamento)
print("Os custos foram de", custo)
print("O lucro final foi de", lucro)
print("A carga tributária foi de", imposto)
print("A margem de lucro foi de", round(margem_lucro, 1))

# mod -> resto da divisão 
tempo_contrato = 170
tempo_anos = 170 /12
print("Tempo em anos", int(tempo_anos))
tempo_meses = 170 % 12
print("Tempo em meses", tempo_meses)





