from datetime import date

print('=== Descubra se Ano é BISSEXTO ===')
ano = int(input('Qual ano deseja analizar? Digite zero para analizar o ano atual: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'O ano {ano} é BISSEXTO.')
else:
    print(f'O ano {ano} não é BISSEXTO.')
