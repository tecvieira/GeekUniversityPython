"""
- Para resolver o problema de enviar dois parametros ao decorators, quando ele só esperava um, usamos *args e **kwargs
este procedimento é chamado de Decorators Patern
- A assinatura de uma função é representada pelo seu retorno, nome e parâmetros de entrada
- Podemos usar parâmetros nomeados

"""


def gritar(funcao):
    def aumentar(*args, **kwargs):
        return funcao(*args, **kwargs).upper()

    return aumentar


@gritar
def saudacao(nome):
    return f'Olá, eu sou o/a {nome}'


@gritar
def ordenar(principal, acompanhamento):
    return f'Olá, eu quero {principal} acompanhado de {acompanhamento}, por favor.'


# testando
print(saudacao('Felicity'))
print(ordenar('picanha', 'Batata Frita'))
print(ordenar(acompanhamento='Batata Frita', principal='Picanha'))
