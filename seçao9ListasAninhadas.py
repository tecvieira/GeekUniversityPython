"""
Listas Aninhadas
Extrutura de dados (arrays) podem ser:
- unidimensionais (arrays/ vetores)
- Multidimensionais (Matrizes) -> Listas Aninhadas em Python

ex01:
listas = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(listas[0][1]) => 2
print(listas[2][1]) => 8

ex02:
listas = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for lista in listas:
    print(lista)

[1, 2, 3]
[4, 5, 6]
[7, 8, 9]

ex03:
listas = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for lista in listas:
    for num in lista:
        print(num)
=>
1
2
3
4
5
6
7
8
9

#List Comprehension
ex03-b:
listas = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
[[print(valor) for valor in lista]for lista in listas]
=>
1
2
3
4
5
6
7
8
9

#Gerando um tabuleiro/ matriz 3 x 3
ex04:
            * esta expressão gera as linha  <->   esta vai gerar as colunas
tabuleiro = [[numero for numero in range(1, 4)] for valor in range(1, 4)]
print(tabuleiro) => [[1, 2, 3], [1, 2, 3], [1, 2, 3]]

#Gerando jogadas para o jogo da velha:
velha = [['X' if numero % 2 == 0 else 'O' for numero in range(1, 4)] for valor in range(1, 4)]
print(velha)
=> [['O', 'X', 'O'], ['O', 'X', 'O'], ['O', 'X', 'O']]

#Gerando Valores iniciais:
print([['*' for i in range(1, 4)] for i in range(1, 4)])
=> [['*', '*', '*'], ['*', '*', '*'], ['*', '*', '*']]

"""
print('Fim...')
