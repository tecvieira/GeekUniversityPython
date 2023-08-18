"""
Higher Order Function -HOF
Indica que uma linguagem de programação que suporta o HOF, retorna outras funções e até mesmo criar variáveis
do tipo funções nos nossos programas.
Em Python, as funções são cidadões de primeira Classe, First Class Citizen.
Exemplos.
"""
def somar(a, b):
    return a + b


def diminuir(a, b):
    return a - b


def multiplicar(a, b):
    return a * b


def dividir(a, b):
    return a / b


def calcular(num1, num2, funcao):
    return funcao(num1, num2)


print(calcular(4, 3, somar))
print(calcular(4, 3, diminuir))
print(calcular(4, 3, multiplicar))
print(calcular(4, 3, dividir))





