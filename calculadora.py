# Interface da calculadora
from calc import soma
from calc import sub

# Apresentação
print('\n\t\t\t -- Calculadora Simples --\n')

# Entradas
n1 = int(input('Informe n1: '))
n2 = int(input('Informe n2: '))

# Processamento
total = soma(n1, n2)
total2 = sub(n1, n2)

# Saída
print(f'{n1} + {n2} = {total}')
print(f'{n1} - {n2} = {total2}')