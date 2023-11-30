from time import sleep


def titulo():
    print("""
       _____________________________
             ÁQUARIO MARINHO
        Calcule quantidaded de sal.
    __________________________________
    """)


def tipo_de_aquario():
    while True:
        try:
            volume = int(input('Quanto de água deseja preparar? '))
        except ValueError:
            print(f'\033[33mErro! O valor deve ser um número inteiro.\033[m ')
            volume = int(input('Quanto de água deseja preparar? '))
        try:
            densidade = int(input('Qual a densidade desejada? '))
        except ValueError:
            print(f'\033[33mErro! o valor deve ser um número inteiro entre 1016 e 1026\033[m')
            densidade = int(input('Qual a densidade desejada? '))
        print("""
        Tipo de aquário:
        01 - FISH Only  (Apenas peixes)
        02 - LPS Corals (corais moles)
        03 - SPS Corals (corais duros)
        """)
        tipo = int(input('Informe o tipo de aquário desejado: '))
        if tipo == 1:
            if densidade == 1023:
                quantidade = volume * 34.5
                return print(f'\033[34mPara {volume} litros de água com densidade de 1023'
                             f' use {quantidade} gramas de sal.\033[m')
            else:
                if densidade <= 1022:
                    print('\033[33mUtilize densidade de 1023 para aquários FISH only.\033[m')
                elif densidade >= 1024:
                    print(f'\033[33mUtilize densidade menor, ideal 1023 para aquários FISH only\033[m')
        elif tipo == 2:
            if densidade == 1025:
                quantidade = volume * 38.0
                return print(f'\033[34mPara {volume} litros de água com densidade {densidade} '
                             f'use {quantidade} gramas de sal\033[m')
            else:
                if densidade <= 1024:
                    print(f'\033[33mCorais LPS (moles), necessitam de densidade maior que {densidade}'
                          f' ideal 1025.\033[m')
                elif densidade >= 1026:
                    print(f'\033[31mAquário para corais LPS (moles),'
                          f' devem utilizar uma densidade menor que {densidade} o ideal é 1025.\033[m')
        elif tipo == 3:
            if densidade == 1026:
                quantidade = volume * 40.5
                return print(f'\033[34mPara {volume} litros de água com densidade {densidade} '
                             f'use {quantidade} gramas de sal\033[m')
            else:
                if densidade >= 1027:
                    print(f'\033[33mA densidade {densidade} pode ser alta para corais SPS,'
                          f' verifique os tipos de corais\033[m')
                elif densidade <= 1025:
                    print(f'\033[33mA densidade {densidade} é baixa para corais SPS\033[m')
        else:
            print('\033[31mERRO! Escolha uma tipo de áquario válido\033[m')
        pergunta = str(input('Deseja continuar? S/N')).strip().upper()
        if pergunta == 'N':
            break


while True:
    titulo()
    print("""
    O que deseja fazer?
    01 - Calcular quantidade de sal necessário para áquario marinho:
    02 - Sair
    """)
    opcao = int(input('Escolha sua opção: '))
    if opcao == 1:
        tipo_de_aquario()
    elif opcao == 2:
        print('Finalizando...')
        sleep(2)
        print('Volte sempre...')
        break
    else:
        print('\033[31mOpção inválida, escolha um valor entre 01 ou 02\033[m')
