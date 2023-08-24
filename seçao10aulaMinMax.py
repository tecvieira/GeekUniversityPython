"""
Exemplos:
lista = [1, 8, 4, 99, 34, 129]
print(max(lista))

dicionario = {'a':1,'b':8,'c':4,'d':99, 'e':44,'f':129}
print(max(dicionario.values()))

dicionario = {'a': 1,'b': 8,'c': 4,'d': 99, 'e':44,'f':129}
print(max(dicionario))

print('Comparando valores com max')
val1 = int(input('Primeiro valor: '))
val2 = int(input('Segundo valor'))
print(max(val1, val2))

musicas = [
    {"titulo": "Tunderstruk", "tocou": 3,},
    {"titulo": "Dead Skim Mask", "tocou": 2},
    {"titulo": "Back in black", "tocou": 4},
    {"titulo": "Too Old to Rrock in roll", "tocou": 32}
]
print('Identificando a mais e menos tocada')
print(max(musicas, key=lambda musica: musica["tocou"]))
print(min(musicas, key=lambda musica: musica["tocou"]))
print('-=' * 35)
print('Desafio imprimir apenas o titulo da mais e menos tocada.')
print(max(musicas, key=lambda musica: musica["tocou"])["titulo"])
print(min(musicas, key=lambda musica: musica["tocou"])["titulo"])
print('-=' * 35)

# outra forma sem o uso de lambda ou funções max() e min()
max = 0
for musica in musicas:
    if musica["tocou"] > max:
        max = musica["tocou"]
for musica in musicas:
    if musica["tocou"] == max:
        print(musica["titulo"])

min = 99999
for musica in musicas:
    if musica["tocou"] < min:
        min = musica["tocou"]
for musica in musicas:
    if musica["tocou"] == min:
        print(musica["titulo"])
"""
print('fim')
