"""
REDUCE
A partir do Python 3 a função reduce() não é mais uma função integrada (built-in). Agora temos
que importar esta função do módulo functools para poder utilizar.

Entendendo o reduce():
    Temos uma coleção de dados:
    dados = [a1, a2, a3,...am, an]
Temos uma função que recebe dois parâmetros, necessário que sejam dois parâmetros:
    def funçao(x, y)
        return x * y
Assim como o MAP() e o FILTER(), a função reduce() recebe dois parâmetros: a função e o iterável

reduce(função, dados)
    Aplicando reduce(), funciona da seguinte forma:
    -Passo 1,
    res1 = f(a1, a2) #Inicia-se com os dois primeiros dados iteráveis o resultado da função é guardado.
    Passo 2,
    res2 = f(res1, a3) # Será aplicado o resultado anterior com o proximo dado, passando na mesma função.
    Este ciclo repete até o último dado de sua coleção.
    Passo n,
    res n= f(res m, an)
A - Aplicando o reduce()

from functools import reduce
dados = [2, 3, 4, 5, 7, 11, 13, 17, 19, 23, 29]

multi = lambda x, y: x * y
res = reduce(multi, dados)
print(res) => 25878772920

B- Comparando com um loop normal
dados = [2, 3, 4, 5, 7, 11, 13, 17, 19, 23, 29]
res = 1
for n in dados:
    res = res * n
print(res) => 25878772920

Obs.: Se não passar dois parâmetros o reduce vai gerar um TypeError,
pois ele sempre espera dois parâmetros.

"""
print('Fim...')

