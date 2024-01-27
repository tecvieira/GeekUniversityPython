def reajusta_salario():
    nome = str(input('Informe o seu nome: '))
    salario = float(input('Informe seu salário bruto: '))
    novo_salario = ((salario * 5) / 100 + salario)
    imposto = (novo_salario * 7) / 100
    salario_liquido = novo_salario - imposto
    print(f'O funcionário, {nome} pagou de imposto R$ {imposto:.2f} seu salário líquido é: R${salario_liquido:.2f} ')


print('==== Calculando seu Salário ====')
reajusta_salario()
