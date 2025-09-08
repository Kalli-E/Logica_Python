
#from signal import pause
import pyautogui as pygui
import time

print(pygui.position())  # Pega a posição do mouse
print(pygui.size())      # Pega a resolução da tela

# Funções de automação do mouse

time.sleep(5)  # Espera 5 segundos para você posicionar o mouse.
print(pygui.position())
pygui.click(button="right")  # Clica na posição atual do mouse. O botão esquerdo é o padrão, se nenhum for especificado
pygui.move(100, 0, duration=1)  # Move o mouse 100 pixels para a direita em 1 segundo
time.sleep(3)  # Espera 3 segundos
pygui.doubleClick()  # Clica duas vezes na posição atual do mouse

# Exemplos da IA
pygui.moveTo(533, 13, duration=1)  # Move o mouse para a posição (533, 13) em 1 segundo
pygui.click()           # Clica na posição atual do mouse
pygui.write('view debug console')  # Escreve o texto 'view debug console' na posição atual do mouse
pygui.sleep = 0.5        # Define um pequeno atraso entre cada caractere digitado
pygui.press('enter')    # Pressiona a tecla 'enter' 
pygui.hotkey('ctrl', 's')  # Pressiona a combinação de teclas 'ctrl + s'

# pygui.alert('Automation complete!')  # Mostra um alerta na tela -> "alert depreciado"

