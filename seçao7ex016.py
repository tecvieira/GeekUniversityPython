from time import sleep
vetor16 = []
n = 0
opcao = ''
print('\033[33mInforme cinco valores reais.\033[m')
while n < 5:
    num = float(input(f'- {n + 1}º valor: '))
    vetor16.append(num)
    n += 1
while True:
    print("""\033[33m
                    OPÇÕES:
    ======================================
    0 - SAIR
    1 - VERIFICAR VALORES EM ORDEM DIRETA
    2 - VER OS VALORES EM ORDEM INVERSA
    ======================================
    \033[m
    """)
    opcao = int(input('\033[33mEscolha uma das opções acima.\033[m'))
    print('-=' * 25)
    sleep(1.5)
    if opcao == 1:
        print(vetor16)
    if opcao == 2:
        vetor16.reverse()
        print(vetor16)
    if opcao == 0:
        break
print('Saindo.....')
sleep(1.5)
print('ByTecVander')
