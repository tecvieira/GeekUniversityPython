vetor15 = []
temporário = []
n = 0

while n < 20:
    num = int(input(f'Informe o {n + 1}º número: '))
    n += 1
    if num not in temporário:
        temporário.append(num)
        print('\033[34mElemento adicionado com sucesso!\033[m')
    else:
        vetor15.append(num)
        print('\033[31mElemento já adicionado, será descartado.\033[m')
print(f'Números adicionados com sucesso! {temporário}')
print(f'Elementos descartados: {vetor15}')
