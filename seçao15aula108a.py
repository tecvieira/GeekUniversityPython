"""
Relembrando Decorators, neste caso o teste foi apenas com um parâmetro e não foi chamada a função
ordenar e por isso não deu TypeError

"""


def gritar(funcao):
    def aumentar(nome):
        return funcao(nome).upper()
    return aumentar


@gritar
def saudacao(nome):
    return f'Olá, eu sou o/a {nome}'


@gritar
def ordenar(principal, acompanhamento):
    return f'Olá, eu quero {principal} acompanhado de {acompanhamento}, por favor.'


print(saudacao('Angelina'))
