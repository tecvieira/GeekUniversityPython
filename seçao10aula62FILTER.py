"""
Ex001.
import statistics

dados = [1.3, 2.7, 0.8, 4.1, 4.3, -0.1]
media = statistics.mean(dados)
print(f'{media}') => 2.183333333333333
res = filter(lambda x: x > media, dados)
print(list(res)) => [2.7, 4.1, 4.3]
print(type(res)) => <class 'filter'>

Ex002.
mport statistics

paises = ['', 'Argentina', '', 'Brasil', 'Chile', '', 'Equador', '', 'Venezuela']
print(paises) => ['', 'Argentina', '', 'Brasil', 'Chile', '', 'Equador', '', 'Venezuela']

res = filter(None, paises)
print(res) => <filter object at 0x7f3550b04040>

print(list(res)) => ['Argentina', 'Brasil', 'Chile', 'Equador', 'Venezuela']

Ex003.
paises = ['', 'Argentina', '', 'Brasil', 'Chile', '', 'Equador', '', 'Venezuela']
res = filter(lambda pais: len(pais) > 0, paises)
print(list(res)) => ['Argentina', 'Brasil', 'Chile', 'Equador', 'Venezuela']

Ex004.

paises = ['', 'Argentina', '', 'Brasil', 'Chile', '', 'Equador', '', 'Venezuela']
res = filter(lambda pais: pais != '', paises)
print(list(res)) => ['Argentina', 'Brasil', 'Chile', 'Equador', 'Venezuela']

#várias formas de obter o mesmo reultado

Ex005.
suarios = [
    {"username":"samuel", 'tweets':['Eu gosto de bolo', 'Eu adoro pizza']},
    {"username":"carla", 'tweets':['Eu gosto de gato']},
    {"username":"samuel", 'tweets':[]},
    {"username":"samuel", 'tweets':['Eu gosto de cachorro', 'Eu vou sair hoje']},
    {"username":"samuel", 'tweets':[]},
]
print(usuarios) => [{'username': 'samuel', 'tweets': ['Eu gosto de bolo', 'Eu adoro pizza']},
                    {'username': 'carla', 'tweets': ['Eu gosto de gato']},
                    {'username': 'samuel', 'tweets': []},
                    {'username': 'samuel', 'tweets': ['Eu gosto de cachorro', 'Eu vou sair hoje']},
                    {'username': 'samuel', 'tweets': []}]

#filtrando os inativos
inativos = list(filter(lambda usuario: len(usuario['tweets']) == 0, usuarios))
print(inativos) => [{'username': 'samuel', 'tweets': []}, {'username': 'samuel', 'tweets': []}]

# Combinar filter e map

nomes = ['Vanessa', 'Ana', 'Maria']
# Crie uma lista contendo a frase 'Sua instrutora é {nome, (com menos de 5 caracteres)}
lista = list(map(lambda nome: f'Sua instrutora é {nome}', filter(lambda nome: len(nome) < 5, nomes)))

print(lista) => ['Sua instrutora é Ana']

"""
print('Filter em 08/07/2023')
