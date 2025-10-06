import selenium
import time
from selenium import webdriver


# Para abrir o navegador
navegador = webdriver.Chrome()

# Acessar um site com Selenium
navegador.get('https://www.python.org/')

#Maximizar janela do navegador
navegador.maximize_window()

# Selecionar um elemento no site
lista_botoes = navegador.find_elements("class name", "button")

# Clicar no elemento
for botao in lista_botoes:
    if "Become a Member" in botao.text:
        botao.click()
        break

time.sleep(10)

# Selecionar uma aba
abas = navegador.window_handles
navegador.switch_to.window(abas[1]) # Muda para a segunda aba (índice 1)

