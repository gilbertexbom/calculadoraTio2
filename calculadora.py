# Interface da calculadora
from calc import soma
from calc import sub

while True:
    # Apresentação
    print('\n\t\t\t -- Calculadora Simples --\n')

    # Menu
    print('1. Soma')
    print('2. Sair')

    # Ler a opção do usuário
    op = int(input('\nOpção: '))

    if op == 1:

        # Entradas
        n1 = int(input('Informe n1: '))
        n2 = int(input('Informe n2: '))

        # Processamento
        total = soma(n1, n2)
        # total2 = sub(n1, n2)

        # Saída
        print(f'{n1} + {n2} = {total}')
        # print(f'{n1} - {n2} = {total2}')
    elif op == 2:
        print('Forte abraço!')
        break
    else:
        print(f'Opção {op} incorreta!')
