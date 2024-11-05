import PySimpleGUI as sg
from time import sleep

sg.theme('reddit')

#layout ... no exemplo criei a variável tela_login para representar a tela de abertura de senha e login. se a tela tem 5 linhas ex: linha
# linha1 (usuario), linha2(colocar o usuário), linha3 (senha), linha4 (coloque a senha), linha5(botão para entrar) então são 4 linhas, nesse caso faço matriz 2x2
# uma lista para cada linha, dentro da linha tela_login
tela_login = [
    [sg.Text('Usuário')],
    [sg.Input(key='usuario')],
    [sg.Text('Senha')],
    [sg.Input(password_char='*', key='senha')],
    [sg.Button('Enviar')],
    [sg.Output(size=(43,10))]
]

#criar a janela
janela = sg.Window('Login',layout=tela_login)

#ler os eventos
while True:
    event,values = janela.read()
    if event == sg.WIN_CLOSED:
        break
    elif event == 'Enviar':
        usuario_digitado = values['usuario']
        senha_digitado = values['senha']
        print('passo 1..feito')
        sleep(5)
        print('passo 2..feito')
        sleep(5)
        print('passo 3..feito')