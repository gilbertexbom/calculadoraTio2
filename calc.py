# Calculadora Simples

def soma(v1, v2):
    return v1 + v2
def sub(v1, v2):
    return v1 - v2
def mult(v1, v2):
    return v1 * v2
def exp(v1, v2):
    return v1 ** v2

def rad(v1):
    return v1 ** (1/2)

# teste
# print(f'{2} + {2} = {soma(2, 2)}')
# print(f'{2} - {2} = {sub(2, 2)}')
# print(f'{2} * {3} = {mult(2, 3)}')
# print(f'{2} ** {3} = {exp(2, 3)}')
print(f'A raíz quadrada de {2} é: {rad(2)}')
