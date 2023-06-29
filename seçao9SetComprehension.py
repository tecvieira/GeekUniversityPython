"""
Set Comprehension:
Segue mesmas condições de antes estudadas
listas = [1, 2, 3, 4, 6, 7]
set = {1, 2, 3, 4, 5, 6, 7}
* set não guarda ordenação

ex01:
numeros = {num for num in range(1, 7)}
print(numeros) => {1, 2, 3, 4, 5, 6}

ex02:
numeros = {x ** 2 for x in range(10)}
print(numeros) => {0, 1, 64, 4, 36, 9, 16, 49, 81, 25}
obs. repare que saída não guarda ordenação

#Transformando a expressão anterior em dicionário:
ex03:
#informe o índice
numeros = {x: x ** 2 for x in range(10)}
print(numeros) => {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}
obs.: os dicionários possuem índice antes de valor.

#Utilizando com string:
obs. Lembre-se em conjunto nao há repetições e ordem.

ex04:
letras = {letra for letra in 'Geek University'}
print(letras) => {'e', 'U', 'y', 'k', 'v', 'r', 'n', 'G', 'i', 't', ' ', 's'}
Obs. repare que não há ordenação e nem repetiçoes de letras

"""
print('fim...')
