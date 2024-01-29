def tamanho_escada():
    degrau = float(input('Informe a distância do primeiro degráu em relação ao solo, (Em cm): '))
    altura_desejada = float(input('Informe a altura que deseja subir (em cm): '))
    conta_degrau = (altura_desejada / degrau) - 1
    print(f'\033[35mPara subir uma altura de {altura_desejada/100} metros sua escada precisa ter {conta_degrau:.0f} '
          f'degraus de {degrau}cm\033[m')


print('\033[34m*** DESCUBRA O TAMANHO DA ESCADA ***\033[m')
tamanho_escada()
