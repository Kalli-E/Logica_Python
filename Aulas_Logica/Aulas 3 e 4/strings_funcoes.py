# strings (informações em texto)
faturamento = 1000
custo = 700
lucro = faturamento - custo

print(f"Faturamento da empresa: {faturamento}, Custo: {custo}, Lucro:{lucro}")

email_cliente = "manoeladasilva@gmail.com"

# @
print(email_cliente.find("@")) # -1 quando não for encontrado

# tamanho do texto
nome_cliente = 'Joao das Couves'

nome_cliente = 'José do Egito'
print(len(email_cliente)) # len -> cotagem de caracteres
print(len(nome_cliente))

#pegar um caracter - solicitar entre chaves []
print(email_cliente[15])
print(nome_cliente[14])

# solicitar caracter do final para o incio
print(nome_cliente[-2])

# solicitar informação a partir de um ponto
print(email_cliente[:7]) 

# solicitar informação a partir de um ponto até um outro ponto
print(email_cliente[0:7])

#replace = substitui uma informação dentro da string
novo_email = email_cliente.replace("gmail.com", "hotmail.com")
print(novo_email)

novo_nome = nome_cliente.replace("do Egito", "da Silva")
print(novo_nome)

# maiúsculo
email_cliente = email_cliente.upper()
print(email_cliente)
# minpusculo
email_cliente = email_cliente.lower()
print(email_cliente)
#Maiusculo e minúsculo - trabalhar com nomes
nome = 'carlos silva'
print(nome.capitalize())
print(nome.title())

#extrair informação de variáveis diferentes
#pegar servidor do e-mail
posicao_arroba = email_cliente.find("@") + 1 # +1 para não pegar o @
servidor = email_cliente[posicao_arroba:]
print(servidor)

#pegar primeiro nome
posicao_espaco = nome.find(" ")
primeiro_nome = nome[:posicao_espaco]
#pegar sobrenome
sobrenome = nome[posicao_espaco + 1 :]
print(primeiro_nome)
print(sobrenome)









