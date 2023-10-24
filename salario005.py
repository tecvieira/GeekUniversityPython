def insal_calc():
    insal_calc = float(((salminimo * insalubre /100) /30) * dias)
    return insal_calc


def feriado_calc():
    feriado_calc = float((salario / 30) * feriado)
    return feriado_calc


def recesso_calc():
    recesso_calc = float((salario / 30) * (30 - dias))
    return recesso_calc


def baseadiant_calc():
    baseadiant_calc = float(salario * adiantamento / 100)
    return baseadiant_calc


def total_proventos():
    total_proventos = float(salario + insal_calc() + feriado_calc())
    return total_proventos

def basecalc_inss():
    basecalc_inss = float(total_proventos() - recesso_calc())
    return basecalc_inss


def inss_calc(basecalc_inss):
    global porcentagem_desconto_inss
    if basecalc_inss <= 1100.00:
        porcentagem_desconto_inss = 7.5
        return (basecalc_inss * 7.5 / 100)
    if 1100.01 <= basecalc_inss <= 2203.48:
        porcentagem_desconto_inss = 9.0
        return ((basecalc_inss - 1100.00) * 9.0 / 100) + 82.5
    if 2203.49 <= basecalc_inss <= 3305.22:
        porcentagem_desconto_inss = 12.0
        return ((basecalc_inss - 2203.48) * 12.0 / 100) + 82.5 + 99.31
    if 3305.23 <= basecalc_inss <= 6433.57:
        porcentagem_desconto_inss = 14.0
        return ((basecalc_inss - 3305.22) * 14.0 / 100) + 82.5 + 99.31 + 132.20
    if basecalc_inss >= 6433.58:
        return 751.98


def depend_calc():
    depend_calc = float(189.59 * dependentes)
    return depend_calc

def baseirrf_adiant():
    baseirrf_adiant = float(baseadiant_calc() + irrfbaseant )
    return baseirrf_adiant


def irpf_calc():
    global desconto_irpf
    if baseirrf_adiant() <= 1903.98:
        desconto_irpf = 0
        return 0
    if 1903.99 <= baseirrf_adiant() <= 2826.65:
        desconto_irpf = 7.5
        return(baseirrf_adiant() * 7.5/100) - 142.8
    if 2826.66 <= baseirrf_adiant() <= 3751.05:
        desconto_irpf = 15
        return(baseirrf_adiant() * 15/100) - 354.8
    if 3751.06 <= baseirrf_adiant() <= 4664.68:
        desconto_irpf = 22.5
        return(baseirrf_adiant() * 22.5/100) - 636.13
    if baseirrf_adiant() >= 4664.69:
        desconto_irpf = 27.5
        return(baseirrf_adiant() * 27.5/100) - 869.36

def adiantamento_irrf():
    adiantamento_irrf = float(irpf_calc() - irrfsalarant)
    return adiantamento_irrf


def adiant_calc():
    adiant_calc = float(baseadiant_calc() - adiantamento_irrf())
    return adiant_calc


def irpfbase_salario():
    irpfbase_salario = float( basecalc_inss() - adiant_calc() - depend_calc() - pensao - adiantamento_irrf() - inss_calc(basecalc_inss()))
    return irpfbase_salario


def salario_irpf():
    global desconto_irpf
    if irpfbase_salario() <= 1903.98:
        desconto_irpf = 0
        return 0
    if 1903.99 <= irpfbase_salario() <= 2826.65:
        desconto_irpf = 7.5
        return(irpfbase_salario() * 7.5/100) - 142.8
    if 2826.66 <= irpfbase_salario() <= 3751.05:
        desconto_irpf = 15
        return(irpfbase_salario() * 15/100) - 354.8
    if 3751.06 <= irpfbase_salario() <= 4664.68:
        desconto_irpf = 22.5
        return(irpfbase_salario() * 22.5/100) - 636.13
    if irpfbase_salario() >= 4664.69:
        desconto_irpf = 27.5
        return(irpfbase_salario() * 27.5/100) - 869.36



def desconto_total():
    desconto_total = float(recesso_calc() + adiant_calc() + inss_calc(basecalc_inss()) + adiantamento_irrf() + salario_irpf() + 28.16)
    return desconto_total


def salario_liquido():
    salario_liquido = float(total_proventos() - desconto_total())
    return salario_liquido


def recebido_total():
    recebido_total = float(salario_liquido() + adiant_calc())
    return recebido_total


salario = float(input('Salário bruto: R$'))
salminimo = float(input('Valor salário mínimo: R$'))
adiantamento = int(input('Percentual de adiantamento no mês. (%)'))
insalubre = int(input('Insalubridade devida (%)'))
dias = int(input('Quantos dias trabalhados?'))
feriado = int(input('Houve feriados? Quantos trabalhou?'))
dependentes = int(input('Dependentes legais, quantos?:'))
pensao = float(input('Pensão alimentícia: R$'))
irrfbaseant = float(input('Base IRRF no mês anterior: R$'))
irrfsalarant = float(input('IRRF desc. salário anterior: R$'))
print()
print('___'*15)
print('             SALÁRIO CALCULADO')
print('___'*15)
print(f'Salario bruto :                   \tR${salario:.2f}')
print(f'Insalubridade:                    \tR${insal_calc():.2f}')
print(f'Feriado trabalhado:               \tR${feriado_calc():.2f}')
print(f'\033[34mTotal de proventos:               \tR${total_proventos():.2f}\033[m')
print('___'*15)
print(f'\033[33mBase cálculo adiantamento:        \tR${baseadiant_calc():.2f}')
print(f'Base de calculo INSS:             \tR${basecalc_inss():.2f}')
print(f'Base de cálculo IRRF no salário:  \tR${irpfbase_salario():.2f}')
print(f'Pensão alimentar (dedução IRRF):  \tR${pensao:.2f}')
print(f'{dependentes} dependentes (dedução IRRF):    \tR${depend_calc()}\033[m')
print('___'*15)
print(f'\033[31mRecesso não remunerado:           \tR${recesso_calc():.2f}')
print(f'Antecipação quinzenal:            \tR${adiant_calc():.2f}')
print(f'Desconto de INSS:                 \tR${inss_calc(basecalc_inss()):.2f}')
print(f'Desc. de IRRF no adiantamento:    \tR${adiantamento_irrf():.2f}')
print(f'Seguro grupo:                     \tR$10.16')
print(f'Contrib. assistencial/ negocial:  \tR$8.00')
print(f'Participação benefício mês atual: \tR$10.00')
print(f'Desc. IRRF no salário:            \tR${salario_irpf():.2f}\033[m')
print('___'*15)
print(f'\033[31mTotal de descontos:               \tR${desconto_total():.2f}\033[m')
print('___'*15)
print(f'\033[34mVALOR LÍQUIDO:                   \tR${salario_liquido():.2f}\033[m')
print()
print(f'\033[33m TOTAL RECEBIDO:                  \tR${recebido_total():.2f}\033[m')
print('___'*15)
print('          By TecVander v1.05')

