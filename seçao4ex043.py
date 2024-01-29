from time import sleep


def calcula_vendas():
    while True:
        valor_original = float(input('Informe valor do ítem: R$ '))
        print("""
                     SUGESTÕES DE PAGAMENTO
                01 - Valor total com desconto de 10%
                02 - Parcelado em 3 vezes sem juros
        * * * Para pagamento total, comissão de 5% sobre valor final para o vendedor * * *
                """)
        resposta = int(input('Informe a opção escolhida: '))
        if resposta == 1:
            desconto10 = (valor_original * 10) / 100
            valor_final = valor_original - desconto10
            print(f'Valor sem desconto: R$ {valor_original:.2f}')
            print(f'Desconto de 10% (R$ {desconto10:.2f}), valor a pagar R$ {valor_final:.2f}')
            print(f'Comissão do vendedor: R$ {valor_final * 5 / 100:.2f}')
            sleep(2)
        if resposta == 2:
            parcelado3 = valor_original / 3
            print(f'Valor sem desconto: R$ {valor_original:.2f}')
            print(f'Valor das 3 parcelas (R$ {parcelado3:.2f})')
            sleep(2)

        print()
        pergunta = str(input('Deseja sair [S/N]')).upper()[0]
        while pergunta not in 'SN':
            print('Informe S para sair ou N para continuar ')
            pergunta = str(input('Deseja sair [S/N]')).upper()[0]
        if pergunta == 'S':
            break


print('==== Assistente de Vendas ====')
calcula_vendas()
print('Finalisando...')
sleep(1)
print('powered by TecVander')
