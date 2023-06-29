"""
list conprehension parte I

Utilizando list conprehension podemos ferar novas listas com dados processados a partir de outro iterável.
#sintaxe ( forma de escrever)
 [dado for dado in iterável]

ex1:
numeros = [1, 2, 3, 4, 5]
res = [numero * 10 for numero in numeros]

print(res)
=> [10, 20, 30, 40, 50]

ex2:
res = [numero / 2 for numero in numeros]
print(res)
=> [0.5, 1.0, 1.5, 2.0, 2.5]

ex3:
def funçao(valor):
    return valor * valor


res = [funçao(numero) for numero in numeros]
print(res)
=> [1, 4, 9, 16, 25]

#Loop
ex01:
numeros = [1, 2, 3, 4, 5]
numeros_dobrados = []

print([numero * 2 for numero in numeros])
=> [2, 4, 6, 8, 10]

ex02:
nome = 'Geek University'
print([letra.upper() for letra in nome]) #coloque cada letra de nome em maiuscula

=> ['G', 'E', 'E', 'K', ' ', 'U', 'N', 'I', 'V', 'E', 'R', 'S', 'I', 'T', 'Y']

ex03:
def caixaAlta(nome):
    nome = nome.replace(nome[0], nome[0].upper())
    return nome


amigos = ['maria', 'julia', 'pedro']
print([caixaAlta(amigo) for amigo in amigos])
=> ['Maria', 'Julia', 'Pedro']

ex04:
print([numero * 3 for numero in range(1, 10)]) # fez um range de 1 a 9 multiplicando cada numero por 3
=> [3, 6, 9, 12, 15, 18, 21, 24, 27]

ex05:
print([bool(valor) for valor in [0, [], '', True, '', 3.14]])
=> [False, False, False, True, False, True]

ex06
#Transformando inteiros em string.
print(str(numero) for numero in [1, 2, 3, 4, 5]])
=> ['1', '2', '3', '4', '5']
============================================================
list conprehension parte II
Podemos adicionar extruturas condicionais lógicas as nossas conprehension
ex01:
numero = [1, 2, 3, 4, 5, 6]
pares =[numero for numero in numero if numero % 2 == 0]
impares = [numero for numero in numero if numero % 2 != 0]

print(pares) => [2, 4, 6]
print(impares) => [1, 3, 5]

ex02:
#Qualquer número par % 2 == 0 (0 em python é False, sendo assim not False = True)
# Qualquer número ímpar % 2 == 1 (1 em Python é True)
numeros = [1, 2, 3, 4, 5, 6]
impares = [numero for numero in numeros if numero % 2]
pares = [numero for numero in numeros if not numero % 2]

print(impares) => [1, 3, 5]
print(pares) => [2, 4, 6]

ex03:
numeros = [1, 2, 3, 4, 5, 6]
res = [numero * 2 if numero % 2 == 0 else numero / 2 for numero in numeros]
print(res)
=> [0.5, 4, 1.5, 8, 2.5, 12]

"""
print('Fim...')
