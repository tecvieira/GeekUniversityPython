def cabecalho():
    print('-=' * 15)
    print('CONVERTA JARDAS EM METROS')
    print('-=' * 15)
    return print()


def converte_valor(vlr):
    return vlr * 0.91


cabecalho()
vlr = int(input('Informe o valor em jardas: '))
print(f'{vlr} JARDAS corresponde a {converte_valor(vlr):.2F} METROS.')

