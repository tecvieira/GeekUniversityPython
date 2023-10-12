"""
Tabalhando com DictWriter
* Observar que as chaves do dicionário devem ser as mesmas utilizadas como cabeçalho, ou seja devem ser escritas da
mesma forma.
* Para criar arquivo novo utiliza-se 'w' se ja possuir um arquivo e quiser adicionar devemos mudar para 'a' .
"""
from csv import DictWriter


with open('filmes2.csv', 'w') as arquivo:
    cabecalho = ['Título', 'Gênero', 'Duração']
    escritor_csv = DictWriter(arquivo, fieldnames=cabecalho)
    escritor_csv.writeheader()
    filme = None
    while filme != 'sair':
        filme = input('Informe nome do filme: ')
        if filme != 'sair':
            genero = input('Informe o gênero: ')
            duracao = input('Informe  duração do filme (em minutos):')
            escritor_csv.writerow({"Título": filme, "Gênero": genero, "Duração": duracao})
