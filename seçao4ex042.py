def gratificacao(sal):
    reajuste = (sal * 5) / 100
    return print(f'Gratificação sobre o salário base R$ {reajuste:.2f}')


def imposto(sal):
    desconto = (sal * 7) / 100
    return print(f'Imposto sobre o salário R${desconto:.2f}')


def saldo_final(sal):
    return sal - desconto + requests


salario = float(input('Informe o salário base: '))
print(f'Salario base.......................R${salario:.2f}')
gratificacao(salario)
imposto(salario)
print(f'Saldo a receber R$ {saldo_final(salario)}')
