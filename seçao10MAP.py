"""
MAP - é uma função que recebe dois parâmetros, o primeiro é uma função o segundo um iterável
retornando um MAP object.

ex01 FORMA COMUM DE RESOLVER
import math


def area(r):
    '''Calcula a área de um círculo com raio r'''
    return math.pi * (r ** 2)


raios = [2, 5, 7.1, 3, 10, 14]
areas = []
for r in raios:
    areas.append((area(r)))


print(areas)

ex02 RESOLVENDO COM MAP e FUNÇÃO

import math


def area(r):
    '''Calcula a área de um círculo com raio r'''
    return math.pi * (r ** 2)


raios = [2, 5, 7.1, 3, 10, 14]

areas = map(area, raios)

print(areas) => <map object at 0x7f74c0219750>
print(type(areas)) => <class 'map'>
print(list(areas)) # vai passar os raios para a função area.
=> [12.566370614359172, 78.53981633974483, 158.36768566746147, 28.274333882308138,
                       314.1592653589793, 615.7521601035994]
ex03 RESOLVENDO COM MAP E LAMBDA

import math


raios = [2, 5, 7.1, 3, 10, 14]

print(list(map(lambda r: math.pi * (r ** 2), raios)))
=> [12.566370614359172, 78.53981633974483, 158.36768566746147, 28.274333882308138, 314.1592653589793, 615.7521601035994]

Obs.: após utilizaçao do resultado da função MAP, esta vai zerar os valores.

Fixando os conceitos:
# Temos dados iteráveis
# Dados a1, a2, a3, ... an
#Temos uma função
# Função: f(x)
# Utilizamos a função map(f, dados) onde map irá mapear cada elemento dos dados e aplicar a funçao
# O MapObject: [f(a1), f(a2), f(a3)]

OUTRO EXEMPLO:
cidades = [('Berlin', 29), ('Cairo', 36), ('Buenos aires', 19), ('Los Angelis', 26), ('Tokio', 27),
           ('Nova York', 28), ('Londres', 22)]
# Converta as temperaturas para fahrenheit.
# f= (9/5) * c + 32

# Criando uma função lambda
c_para_f = lambda dado: (dado[0], (9/5) * dado[1] + 32)

# executando uma função lambda direto no print
print(list(map(c_para_f, cidades)))

=> [('Berlin', 84.2), ('Cairo', 96.8), ('Buenos aires', 66.2), ('Los Angelis', 78.80000000000001),
    ('Tokio', 80.6), ('Nova York', 82.4), ('Londres', 71.6)]

"""
print('Fim')







