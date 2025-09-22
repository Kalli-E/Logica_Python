# Criar uma classe para os clientes do netflix 

from tokenize import PlainToken


class Cliente():
    def __init__(self, nome, email, plano):
        self.nome = nome,
        self.email = email,

        self.lista_planos = ["Básico", "Premium"]
        if plano in self.lista_planos:
            self.plano = plano
        else:
            raise Exception("Plano inválido!") #serve para criar uma exceção, onde o programa para de rodar e mostra a mensagem de erro
        
    def mudar_plano(self, novo_plano):
        if novo_plano in self.lista_planos:
            self.plano = novo_plano
        else:
            print("Plano Inválido!")

    # def ver_filmes(self, filme):
    


cliente = Cliente("João", "joao@email.com", "Premium")
print(cliente.nome, cliente.plano)

cliente.mudar_plano(input("Digite o novo plano: ").lower)
if cliente.plano in cliente.lista_planos:
    print("Plano alterado com sucesso!")
else:
    print("Não foi possível alterar o plano!")
