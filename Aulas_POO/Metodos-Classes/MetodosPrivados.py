# Conceitos Iniciais

# class MinhaClasse:
#     def __init__ (self, info, elemento):
#         self.atributo_1 = 'Meu atributo'
#         self.atributo_2 = 'elemento'
#         self.atributo_3 = [1,2,'a']
#         self.atributo_4 = info
#         print (self.atributo_4)  

# def metodo_1(self):
#     print("minha ação 1")
#     print("minha ação 2")
#     print(self.atributo_2)
#     return "Olá mundo"

# def metodo_2 (self, numero):
#     self.metodo_1()
#     print(self.atributo3[1] + numero)

# minha_classe = MinhaClasse("informação", 213)
# minha_classe.metodo_2(3)
    
class Pessoa:
    def __init__(self, altura, cpf) -> None:
        self.altura = altura
        self.__cpf = cpf

    def apresentar(self):
        print(f'Minha Altura - {self.altura}')
        self.__coletar_documento() # Chamando o método privado dentro de um método público

    def __coletar_documento(self): # Definimos uma função privada dentro da classe
        print(f'Meu Documento - {self.__cpf}')

joao = Pessoa("1,80", "111.222.333-44")
joao.apresentar() # A forma de apresentar o cpf, que está como privado, foi referencia-lo  em outro método da classe, que seria o "apresentar."


## O def __ (dois underlines) antes de um atributo ou método torna ele privado, ou seja, não pode ser acessado fora da classe.
## Mesmo que você tente criar um atributo com o mesmo nome fora da classe, ele não irá sobrescrever o atributo privado original.
## A tentativa de acessar um atributo ou método privado fora da classe resultará em um erro de atributo.
## o método def serve para definir funções dentro de uma classe, que são chamadas de métodos.
## Métodos privados são úteis para encapsular funcionalidades internas que não devem ser expostas ao usuário da classe.

