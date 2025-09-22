import selenium
import time
from selenium import webdriver
# from selenium.webdriver.common.by import By

# Para abrir o navegador
navegador = webdriver.Chrome()

# Acessar um site com Selenium
navegador.get('https://google.com')
# navegador.get('https://cursoautomacao.netlify.app/')

#Maximizar janela do navegador
navegador.maximize_window()

navegador.find_element('name', 'q').send_keys('Curso de automação web com Python') # Localiza a barra de pesquisa pelo nome e digita o texto
navegador.find_element('name', 'q').submit()    # Envia o formulário (equivalente a pressionar Enter)

time.sleep(10) # O navegador só é fechado após ele terminar de carregar, somado aos 10 segundos de espera


