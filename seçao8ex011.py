def nota_final():
    nota1 = float(input(f'Nota da 1ª prova:'))
    nota2 = float(input(f'Nota da 2ª prova:'))
    nota3 = float(input(f'Nota da 3ª prova:'))
    soma = nota1 + nota2 + nota3
    print("\n"
          "          Selecione a opçãp:      \n"
          "    -------------------------------\n"
          "    A - média aritmética\n"
          "    P - Média ponderada por pesos \n"
          "    -------------------------------\n"
          "    ")
    res = ''
    mponderada = 0
    resp = str(input('Qual a sua opção: ')).strip().upper()
    if resp == 'A':
        aritimética = soma / 3
        print(f'A média aritmética é {aritimética}')
    elif resp == 'P':
        peso1 = int(input('Peso da 1ª nota: '))
        peso2 = int(input('Peso da 2ª nota: '))
        peso3 = int(input('Peso da 3ª nota'))
        mponderada = ((nota1 * peso1) + (nota2 * peso2) + (nota3 * peso3)) / (peso1 + peso2 + peso3)
        print(f'A média ponderada é {mponderada}')


nota_final()
