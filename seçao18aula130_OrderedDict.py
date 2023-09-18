from csv import DictReader


with open('lutadores.csv') as arquivo:
    leitor_csv = DictReader(arquivo)
    for linha in leitor_csv:
        print(f"{linha['Nome']} nasceu {linha['País']} mede {linha['Altura (em cm)']}")
