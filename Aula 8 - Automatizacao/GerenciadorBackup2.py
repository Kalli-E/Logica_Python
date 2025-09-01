import os
import tkinter #pesquisar
import shutil

from tkinter.filedialog import askdirectory #quando importar, esta ordem não pode ser invertida.

caminho_pasta_selecionada = askdirectory()
print(caminho_pasta_selecionada) #Resultado ex: C:/Users/Aluno.LABINFO06/Documents/repoLocal/Aula 8

lista_arquivos = os.listdir(caminho_pasta_selecionada)
print(lista_arquivos) #Resultado ex: ['Backup Teste', 'GerenciadorBackup.py']

nome_pasta_backup = "Backup Teste"
nome_completo_pasta_backup = f"{caminho_pasta_selecionada}/{nome_pasta_backup}"  #serve para criar uma pasta dentro do caminho selecionado

if os.path.exists (nome_completo_pasta_backup):
    print("Pasta já existe no sistema!")
if not os.path.exists(nome_completo_pasta_backup):
    os.mkdir(nome_completo_pasta_backup)
    print("Pasta criada com sucesso!")

for arquivo in lista_arquivos:
    print(arquivo) # Resultado ex: Backup teste, GerenciadorBackup.py

    nome_completo_arquivo = f"{caminho_pasta_selecionada}/{arquivo}"
    nome_final_arquivo = f"{nome_completo_pasta_backup}/{arquivo}"

    if "." in arquivo:
        shutil.copy2(nome_completo_arquivo, nome_final_arquivo)
        print(nome_completo_arquivo, nome_final_arquivo, "\n")

    elif "Backup Teste" != arquivo:
        shutil.copytree(nome_completo_arquivo, nome_final_arquivo)
        print(nome_completo_arquivo, nome_final_arquivo)



