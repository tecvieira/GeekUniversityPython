"""
Sintaxe:
{ chave: valor for valor in iterável}

ex01:
numeros = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5}
quadrado = {chave: valor ** 2 for chave, valor in numeros.items()}
print(quadrado) => {'a': 1, 'b': 4, 'c': 9, 'd': 16, 'e': 25}
Obs.: Manteve as chaves e alterou os valores conforme expessão (chave: valor ** 2 for chave)

ex02:
numeros = [1, 2, 3, 4, 5]
quadrados = {valor: valor ** 2 for valor in numeros}
print(quadrados) => {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
criou o indice de forma ordenada e os valores aplicando a expressão (valor**2) valor ao quadrado.

ex03:
chaves = 'abcde'
valores = [1, 2, 3, 4, 5]
mistura = {chaves[i]: valores[i] for i in range(0, len(chaves))}
print(mistura) => {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

ex04:
numeros = [1, 2, 3, 4, 5]
res = {num: ('par' if num % 2 == 0 else 'impar') for num in numeros}
# os números serão o índice e os valores vao alternar par ou impar conforme o índice.
print(res) => {1: 'impar', 2: 'par', 3: 'impar', 4: 'par', 5: 'impar'}

"""
print('Fim...')


