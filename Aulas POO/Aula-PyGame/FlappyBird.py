import pygame 
import os
import random

TELA_LARGURA = 500
TELA_ALTURA = 800

IMG_CANO = pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'pipe.png')))
IMG_CHAO =  pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'base.png')))
IMG_BCKGRND = pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'bg.png')))
IMGS_PASSARO = [
                pygame.transform.scale2x(pygame.image.load(os.path.join('imgs','bird1.png'))),
                pygame.transform.scale2x(pygame.image.load(os.path.join('imgs','bird2.png'))),
                pygame.transform.scale2x(pygame.image.load(os.path.join('imgs','bird3.png')))]

pygame.font.init()
FONTE_PONTOS = pygame.font.SysFont('cambria', 50)

class Passaro:
    IMGS = IMGS_PASSARO 

    # Animações da rotação
    ROTACAO_MAXIMA = 25
    VELOCIDADE_ROTACAO = 20
    TEMPO_ANIMACAO = 5

    def __init__ (self, x, y):
        self.x = x
        self.y = y
        self.angulo = 0
        self.velocidade = 0
        self.altura = self.y
        self.tempo = 0
        self.contagem_imagem = 0
        self.imagem = IMGS_PASSARO [1]

    def pular(self):
        self.velocidade = 10.5
        self.tempo = 0
        self.altura = self.y

    def mover(self):
        #Calcular o deslocamento
        self.tempo +=1
        deslocamento = 1.5 * (self.tempo**2) + self.velocidade * self.tempo

        #Restringir o deslocamento
        

        #Ângulo do pássaro

class Cano:
    pass

class Chao:
    pass