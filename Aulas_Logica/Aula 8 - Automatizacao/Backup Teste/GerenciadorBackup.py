import os
import tkinter #pesquisar
import shutil

from tkinter.filedialog import askdirectory #quando im0ortar, esta ordem não pode ser invertida

caminho_pasta_selecionada = askdirectory()
print(caminho_pasta_selecionada)

lista_arquivos = os.listdir(caminho_pasta_selecionada)
print(lista_arquivos)

nome_pasta_backup = "Backup Teste"
nome_completo_pasta_backup = f"{caminho_pasta_selecionada}/{nome_pasta_backup}"  #serve para criar uma pasta dentro do caminho selecionado
if os.path.exists (nome_completo_pasta_backup):
    print("Pasta já existe no sistema!")
if not os.path.exists(nome_completo_pasta_backup):
    os.mkdir(nome_completo_pasta_backup)
    print("Pasta criada com sucesso!")

for arquivo in lista_arquivos:
    print(arquivo)
    

