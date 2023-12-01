# Interface da calculadora
import calc

# Apresentação
print('\n\t\t\t -- Calculadora Simples --\n')

# Entradas
n1 = int(input('Informe n1: '))
n2 = int(input('Informe n2: '))

# Processamento
total = calc.soma(2, 2)

# Saída
print(f'{n1} + {n2} = {total}')