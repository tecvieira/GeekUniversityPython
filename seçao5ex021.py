opçao = 0
resp = ' '
while opçao != 5:
    num = float(input('Informe um número inteiro: '))
    num2 = float(input('Informe outro número: '))
    print("""
    [1] Somar dois números
    [2] Diferença entre dois números
    [3] Multiplicar dois números
    [4] Dividir  dois números
    [5] Sair
    """)
    opçao = int(input('O que deseja fazer? '))
    if opçao == 1:
        print(f'A soma dos números {num} e {num2} é igual a {num + num2}')
    elif opçao == 2:
        print(f'A diferença dos números {num} e {num2} é igual a {num - num2}')
    elif opçao == 3:
        print(f'A multiplicação dos números {num} e {num2} é igual a {num * num2}')
    elif opçao == 4:
        print(f'A divisão dos números {num} e {num2} é igual a {num / num2}')
    elif opçao == 5:
        print('Finalizando....')
        break
    else:
        print('Opção inválida! Escolha um valor entre 1 e 5: ')



