nota = 10.0
somanota = 0
total = 0
while nota != 0:
    try:
        nota = float(input('Informe uma nota entre 10 e 20 pontos. (zero para sair): '))
        if 10.0 <= nota <= 20.0:
            total += 1
            somanota += nota
            if nota == 0:
                total -= 1
        else:
            print(f'\033[31mNota {nota} não permitida!\033[m')
    except (ValueError, ZeroDivisionError):
        print(f'\033[31mVoce digitou um valor inválido!\033[m')
try:
    media = somanota / total
except ZeroDivisionError:
    media = 0
    print(f'\033[31mUsuário preferiu sair e nao informou nota alguma.\033[m]')
if total == 0:
    print('Finalizando...')
else:
    print('=' * 29)
    print('          RELATÓRIO')
    print('=' * 29)
    print(f'Foram informados {total} nota(s) - Total de pontos: {somanota}')
    if media <= 9.9:
        print(f'Sua média, {media:.2f} - Situação: "\033[31mAluno Reprovado\033[m]"')
    elif 10.0 <= media <= 16.99:
        print(f'Sua média: {media:.2f} - Situaçao: "\033[33mAluno em Recuperaçao\033[m]"')
    elif media >= 17.0:
        print(f'Sua média, {media:.2f} - Situação: "\033[34mAluno Aprovado\033[m]"')
    print()
    print('\033[35mSempre esteja atualizando-se!!!\033[m]')
