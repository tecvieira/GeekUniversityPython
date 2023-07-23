"""
Zip()
Cria um iterável (zip object) que agrega elementos de cada um dos iteráveis passados como entrada em pares.

Ex001
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
zip1 = zip(lista1, lista2)
print(zip1) => <zip object at 0x7f82b0ca1ac0>
print(type(zip1)) => <class 'zip'>

Ex002:
Gerando uma lista com zip:
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
zip1 = zip(lista1, lista2)
print(list(zip1)) => [(1, 4), (2, 5), (3, 6)]

Ex003:
Gerando uma tupla com zip.

lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
zip1 = zip(lista1, lista2, 'abc')
print(tuple(zip1)) => ((1, 4, 'a'), (2, 5, 'b'), (3, 6, 'c'))

Ex004:
Gerando um set com zip.
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
zip1 = zip(lista1, lista2, 'abc')
print(set(zip1)) => {(1, 4, 'a'), (2, 5, 'b'), (3, 6, 'c')}

Ex005:
Gerando um diconário com zip.
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
zip1 = zip(lista1, lista2)
print(dict(zip1)) => {1: 4, 2: 5, 3: 6}

Ex006:
iIteráveis com quantidade diferente de variáveis.
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
lista3 = [7, 8, 9, 10, 11]
zip1 = zip(lista1, lista2, lista3)
print(list(zip1)) => [(1, 4, 7), (2, 5, 8), (3, 6, 9)]

Observe que a saída será limitada pelo menor tamanho dos itráveis, no caso acima os dois últimos
de lista3 foram descartados.

Ex007:
Utilizando zip com iteráveis de tipo diferente:

tupla = (1, 2, 3, 4, 5)
lista = [6, 7, 8, 9, 10]
dicionario = {'a': 11, 'b': 12, 'c': 13, 'd': 14, 'e': 15}
zt = zip(tupla, lista, dicionario.values())
print(list(zt)) => [(1, 6, 11), (2, 7, 12), (3, 8, 13), (4, 9, 14), (5, 10, 15)]

Ex008:
Aplicando zip em uma lista de tuplas:

dados = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5)]
print(list(zip(*dados))) => [(0, 1, 2, 3, 4), (1, 2, 3, 4, 5)]
Obs. O zip vai pegar o primeiro elemento de cada tupla e formar uma nova, os demais elementos formaram outra tupla.

Ex009:
Exemplos mais complexos:

prova1 = [80, 90, 78]
prova2 = [98, 89, 53]
alunos = ['maria', 'pedro', 'carla']
final = {dado[0]: max(dado[1], dado[2]) for dado in zip(alunos, prova1, prova2)}
print(final) => {'maria': 98, 'pedro': 90, 'carla': 78}

"""
print('Fim...')
