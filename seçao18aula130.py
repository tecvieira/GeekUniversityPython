from csv import reader


with open('lutadores.csv') as arquivo:
    leitor_csv = reader(arquivo)
    next(leitor_csv)
    for linha in leitor_csv:
        print(f'{linha[0]} nasceu em {linha[1]} e mede {linha[2]}')
