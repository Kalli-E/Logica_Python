# A pasta "arquivos" foi adicionada ao repositório. Ela está localizada no moodle, em "Códigos das aulas - arquivos.rar"
import os
#import datetime
#import pyautogui # É necessário instalar a biblioteca pyautogui no prompt de comando -> ver "anotações.md"

#pyautogui.press("win") #um comando para o python apertar o botão do menu windows
#pyautogui.write("vscode") #um comando para o python escrever "vscode" na barra de pesquisa

print(os.listdir("arquivos"))
#print (datetime.date.today()) # Os parêntesis vazios indicam que não tem nenhum parâmetro específico para a função solicitada

lista_arquivos = os.listdir("arquivos")
for arquivo in lista_arquivos:
 if ".txt" in arquivo:
    #print("Movimentar", arquivo)
    if "22" in arquivo:
      os.rename(f"arquivos/{arquivo}", f"arquivos/22/{arquivo}")
      #print("Movimentar ", arquivo, "para a pasta 22.")

    elif "23" in arquivo:
      #print("Movimentar ", arquivo, "para a pasta 23." )
      os.rename(f"arquivos/{arquivo}", f"arquivos/23/{arquivo}")



lista_arquivos_retorno22 = os.listdir("arquivos/22")
for arquivo in lista_arquivos_retorno22:
  if ".txt" in arquivo:
    if "22" in arquivo:
      os.rename(f"arquivos/22/{arquivo}", f"arquivos/{arquivo}")



lista_arquivos_retorno23 = os.listdir("arquivos/23")
for arquivo in lista_arquivos_retorno23:
  if ".txt" in arquivo:
    if "23" in arquivo:
      os.rename(f"arquivos/23/{arquivo}", f"arquivos/{arquivo}")



