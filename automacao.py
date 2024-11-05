''' automizar as msg para meus clientes no whatsapp
 primeiro passo: onde esta sendo feito? (whatsapp web)
 quais tec preciso para resolver essas demandas? - teclado(Pyautogui), -acesso ao site(webbrowser), -automatizar digitação(link zap),
 -automaztizar leitura de dados (biblioteca openpyxcl)'''

import openpyxl
from urllib.parse import quote
import webbrowser
# Descrever os passos manuais e dps transforma em código
# ler planilha, e guardar informações, sobre condiçoes, eventos, e etc
workbook = openpyxl.load_workbook('Relação Thales Ligação.xlsx')
pagina_clientes = workbook['Plan1']

for linha in pagina_clientes.iter_rows(min_row=1):
    #nome, telefone, informação passar cliente
    nome = linha[0].value
    ddd = linha[3].value
    telefone = linha[4].value
    msg = f'Olá {nome} você tem interesse em saber condições imperdíveis da Volkswagen para esse final de mês? 
    
    link_msg_zap = f'https://web.whatsapp.com/send?phone={telefone}&text={quote(msg)}'
    webbrowser.open(link_msg_zap)
    # https://web.whatsapp.com/send?phone=83986231197&text


# criar links personalizados do zap e enviar msg para cada cliente  com base nos dados da planilha

