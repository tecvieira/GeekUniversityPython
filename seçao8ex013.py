def escolhe_sinal(a, b):
    sinal = ''
    sinal = input('Sinal da operação ("+", "-", "*", "/" ), escolha sua opção: ')
    if sinal == '+':
        print(a + b)
    elif sinal == '-':
        print(a - b)
    elif sinal == '*':
        print(a * b)
    elif sinal == '/':
        print(a / b)
    else:
        print('Valor inválido, tente outra vez')


escolhe_sinal(a=int(input('Valor de "a": ')), b=int(input('Valor de "b": ')))
