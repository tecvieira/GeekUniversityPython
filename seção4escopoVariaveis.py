# variavel local
numero = 42
print(numero)
print(f'Esta variável {numero} têm sua classe do tipo: {type(numero)}')

numero = 'Geek'
print(numero)
print(f'Esta variável {numero} têm sua classe do tipo: {type(numero)}')

numero = 42
if numero > 10:
    novo = numero + 10
# nesnte caso novo é uma variável local, só exite dento do bloco ou quando a condição for verdadeira
print(novo)
