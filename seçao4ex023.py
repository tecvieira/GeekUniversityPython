while True:
    print("""
    === CONVERTA SUA MEDIDA ===
    0 - SAIR
    1 - CONVERTE JARDAS EM METRO
    2 - CONVERTE METRO EM JARDAS
    """)
    opcao = int(input('Escolha  sua opção ou zero para sair: '))
    if opcao == 1:
        med = float(input('Informe o valor: '))
        print(f'\033[32mO valor de {med} JARDAS corresponde: {med * 0.91:.2f} METROS.\033[m')
    if opcao == 2:
        med = float(input('Informe o valor: '))
        print(f'\033[32mO valor de {med} METROS corresponde: {med / 0.91:.2f} METROS.\033[m')
    if opcao == 0:
        print('Saindo do sistema...')
        break
print('\033[31mBy TecVander...')
