# Automação com PyAutoGUI.  SO: Windows 10 versão 22H2. Resolução da tela: 1600x900

import pyautogui as pygui
import time

print(pygui.position())  # Pega a posição do mouse
print(pygui.size())      # Pega a resolução da tela

# Funções de automação do mouse (em uma tela de resolução 1600X900)

pygui.FAILSAFE = False  # Desativa o failsafe (movimento do mouse para o canto inferior direito da tela)
pygui.PAUSE = 1    # Define uma pausa de 1 segundo entre as ações

time.sleep(3)  # Espera 3 segundos para você posicionar o mouse
pygui.click(x=13, y=883, clicks=1, button='right', duration=0.75) # Clica na posição (13, 883) uma vez com o botão direito
pygui.click(x=26, y=689, clicks=2, button='left', duration=0.75) # Clica na posição (26, 689) duas vezes

#pygui.moveTo(0, 0, duration=1)  # Move o mouse para a posição (0, 0) (canto superior esquerdo) em 1 segundo

print(pygui.position()) #imprime no console a posição atual do mouse
pygui.moveTo(800,450, duration=1)  # Move o mouse para a posição (800, 450) (centro da tela) em 1 segundo
print(pygui.position())
pygui.click(pygui.moveTo(225, 355, duration=1))
pygui.scroll(-500)  # Rola a tela para baixo 500 "unidades"

# Funções do teclado
pygui.move(0,-250, duration=1) # Move o mouse 250 pixels para cima em 1 segundo
pygui.click()
pygui.write('alterar', interval=0.1)  # Digita o texto com um intervalo de 0.1 segundos entre cada letra
pygui.press('enter')  # Pressiona a tecla 'enter'
pygui.press('enter')

pygui.moveTo(1560, 20, duration=1)  # Move o mouse 1560 pixels para a direita e 20 pixels para baixo em 1 segundo (canto superior esquerdo da tela)

pygui.click()  # Clica uma vez na posição atual do mouse
pygui.moveTo(800,450, duration=1) # volta para o centro da tela

pygui.hotkey("win","s")  # Pressiona a combinação de teclas 'windows + s'
pygui.write("cmd", interval=0.1) 
pygui.press("enter")
time.sleep(1)  # Espera 1 segundo
pygui.write("tracert www.oi.com.br", interval=0.1)
pygui.press("enter")
time.sleep(10)
pygui.hotkey("ctrl","c")
pygui.write("ping 192.168.205.1 -t", interval=0.3)
pygui.press("enter")
time.sleep(10)
pygui.hotkey("ctrl","c")
pygui.write("exit", interval=0.1)
pygui.press("enter")


# pygui.click(pygui.position())


# Observações:
## OBS: o comando moveTo() move o mouse para uma posição absoluta na tela, enquanto o comando move() move o mouse em relação à sua posição atual.
## OBS2: o comando 'pygui.FAILSAFE = False' desativa o failsafe, que é uma medida de segurança que faz o programa parar se o mouse for movido para o canto superior esquerdo da tela, ou para o canto inferior direito da tela.
## OBS3: o comando 'pygui.PAUSE = 5' define uma pausa de 5 segundos entre as ações do pyautogui, para evitar que o programa execute as ações muito rapidamente.
## OBS4: a diferença entre o comando "duration" e o comando "interval" é que o comando "duration" define o tempo que o mouse leva para se mover de uma posição para outra, enquanto o comando "interval" define o tempo entre os cliques quando o número de cliques é maior que 1.