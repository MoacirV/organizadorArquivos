#importação das bibliotecas necessárias
import os
from tkinter.filedialog import askdirectory

# Abre uma janela para o usuário selecionar a pasta que deseja organizar
caminho = askdirectory(title="Selecione uma pasta organizar")

# Lista todos os arquivos na pasta selecionada pelo usuário
lista_arquivos = os.listdir(caminho)

locais = {
    #pasta  | extensões
    "imagens": [".png", ".jpg", ".webp", ".jpeg", ".bmp", ".tiff", ".gif"],
    "planilhas": [".xlsx", ".xlsm", ".xls", ".xlsb", ".dif", ".csv"],
    "pdfs": [".pdf"],

}
# Itera sobre cada arquivo na pasta selecionada 
for arquivo in lista_arquivos:
    # Verifica em qual categoria o arquivo se encaixa com base em sua extensão
    nome, extensao = os.path.splitext(f"{caminho}/{arquivo}")
    for pasta in locais: 
        if extensao in locais[pasta]:
            # Verifica se a pasta correspondente à categoria existe; se não, cria a pasta
            if not os.path.exists(f"{caminho}/{pasta}"):
                os.mkdir(f"{caminho}/{pasta}")
                # Move o arquivo para a pasta correspondente
            os.rename(f"{caminho}/{arquivo}", f"{caminho}/{pasta}/{arquivo}")
            break  