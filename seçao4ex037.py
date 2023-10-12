def desconto_produto(x):
    vlr_final =x - (x * (12/100))
    print(f'\033[34mDesconto promcional 12% - valor: R$ {vlr_final:.2f}\033[m')


produto = float(input('Informe o valor do produto: '))
desconto_produto(produto)