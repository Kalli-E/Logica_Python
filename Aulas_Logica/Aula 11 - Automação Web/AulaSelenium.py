import selenium
import time
from selenium import webdriver


# Para abrir o navegador
navegador = webdriver.Chrome()

# Acessar um site com Selenium
navegador.get('https://ge.globo.com')

#Maximizar janela do navegador
navegador.maximize_window()

# Selecionar um elemento no site
botao_menu = navegador.find_element("class name", "menu-button")

# Clicar no elemento
botao_menu.click()

time.sleep(5)

#Selecionar outro elemento no site
botao_pesquisa = navegador.find_element('name', 'q')

botao_pesquisa.send_keys('brasileirão') # Localiza a barra de pesquisa pelo nome e digita o texto

botao_pesquisa.submit()    # Envia o formulário (equivalente a pressionar Enter)

    # Elemento em html:
        # <input placeholder="BUSCAR" type="search" name="q" id="busca-campo" autocomplete="off" tabindex="1">
    
    # No elemento acima, o atributo name="q" é o que estamos utilizando para localizar o campo de pesquisa. Ele pode ser modificado para qualquer outro elemento. É equivalente ao dicionário [chave, valor] em Python.

time.sleep(30) # O navegador só é fechado após ele terminar de carregar, somado aos 10 segundos de espera


# OBS: o "q" é o nome do campo de pesquisa do Google. Pode ser verificado inspecionando o elemento no navegador (clicar com o botão direito na barra de pesquisa e selecionar "Inspecionar").
# OBS2: O comando 'navegador.find_element' localiza um elemento na página
# OBS3: o "name" é um dos vários métodos de localização de elementos disponíveis no Selenium. Outros métodos incluem "id", "class name", "tag name", "xpath", entre outros. Neste caso, ele significa que o elemento será localizado pelo atributo "name".
# OBS4: o comando 'send_keys' simula a digitação de texto em um campo de entrada.

