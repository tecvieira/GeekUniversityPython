def mostraData(a, b, c):
     print('==='*16)
     print(f'{a} de {b} de {c}, foi o dia do seu nascimento.')


ano = ('Valor inválido', 'janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro',
      'outubro', 'novoembro', 'dezembro')
mostraData(a=int(input('Dia em que nasceu: ')),
           b=ano[int(input('Mês que nasceu: em número'))],
           c=int(input('Ano de seu nascimento:')))
