"""
No switch o conteúdo de uma variável é comparado com um valor constante e, caso a comparação seja verdadeira,
um determinado comando é executado. O switch pode ser usado por exemplo para criar um menu com opções onde o usuário
escolhe uma das opções e instruções são executadas de acordo com essa escolha.
No Python não temos o switch, porém, podemos implementar algo parecido usando dicionários.
"""

semana = {1:'domingo', 2: 'segunda', 3: 'terça', 4: 'quarta', 5: 'quinta', 6: 'sexta', 7: 'sábado'}
res = ''
while True:
    dia = int(input('Escolha um valor entre 1 e 7 e veja o dia da semana: '))
    if dia < 0 or dia > 7:
        print(' Valor inválido!!!')
    if 0 < dia <= 7:
        print(semana[dia])
        res = str(input('Deseja continuar? S/N')).strip().upper()
        if res == 'N':
            break
print('Volte sempre...')
