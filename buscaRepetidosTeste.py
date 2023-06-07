dados = ['laranja', 'banana', 'maçã', 'mprango', 'uva', 'pera', 'maçã', 'limão', 'banana', 'laranja']
valores = []
repetidos = set()
for dado in dados:
    if dado not in valores:
        valores.append(dado)
    else:
        repetidos.add(dado)
print(f'Valores = {valores}')
print(f'Repetidos = {repetidos}')
