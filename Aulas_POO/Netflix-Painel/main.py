class ControleRemoto:
    def __init__(self, cor, altura, profundide, largura):
     self.cor = cor
     self.altura = altura
     self.profundide = profundide
     self.largura = largura

    def mudar_volume(self, botao):
        if botao == "+":
           print("Aumentando o volume")
        elif botao == "-":
           print("Diminuindo o volume")

controle1 = ControleRemoto("branca", "10cm", "2cm", "3cm")
controle1.mudar_volume("+")
controle2 = ControleRemoto("preta", "15cm", "5cm", "5cm")
print(controle2.cor)
controle2.mudar_volume("-")

print(controle1.cor)
print(controle1.altura)
print(controle2.cor)
    # Métodos
    # - power (liga/desliga)
    # - mexer no volume
    # - mute
    # - menu