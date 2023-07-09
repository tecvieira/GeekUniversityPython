opcao = 0
while opcao != 5:
    print('====== CALCULADORA ======')
    print("""
    [1] - SOMA
    [2] - SUBTRAÇAO
    [3] - MULTIPLICAÇÃO
    [4] - DIVISÃO
    [5] - SAIR
    """)
    print('---' * 8)
    opcao = int(input('Qual a sua opção: '))
    print()
    if 0 < opcao <= 4:
        num = int(input('Informe um número inteiro: '))
        num2 = int(input('Informe outro número: '))
        if opcao == 1:
            print(f'\033[34m{num} + {num2} = {num+num2}\033[m')
        elif opcao == 2:
            print(f'\033[34m{num} - {num2} = {num - num2}\033[m')
        elif opcao == 3:
            print(f'\033[34m{num} x {num2} = {num * num2}\033[m')
        elif opcao == 4:
            print(f'\033[34m{num} / {num2} = {num / num2}\033[m')
        else:
            print('\033[31mOpção inválida! Digite novamente.\033[m ')
    elif opcao == 5:
        print('\033[35mFinalizando...\033[m')
        break
    else:
        print('\033[31mOpção inválida!.\033[m ')
print('\033[35m-=-=' * 10)
print('By TecVander')



