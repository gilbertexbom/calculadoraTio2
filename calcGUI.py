# Interface Gráfica com o Usuário

import PySimpleGUI as psg

from calc import soma

layout = [
    [psg.Text('Informe N1: '), psg.InputText(key='Num1')],
    [psg.Text('Informe N2: '), psg.InputText(key='Num2')],
    [psg.Text('', key='Total')],
    [psg.Button('Calcular')],
]

janela = psg.Window('Calculadora Simples', layout)

while True:
    eventos, valores = janela.read()

    if eventos == psg.WIN_CLOSED:
        break
    else:
        n1 = int(valores['Num1'])
        n2 = int(valores['Num2'])
        total = soma(n1, n2)
        janela['Total'].update(total)

janela.close()


