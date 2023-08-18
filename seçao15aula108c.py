"""
Decorators com parametros
O parâmetro passado no decoretor vai determinar a possibilidade de execução da função, senão for atendido
dispara a mensagem de erro
"""


def verifica_primeiro_argumento(valor):
    def interna(funcao):
        def outra(*args, **kwargs):
            if args and args[0] != valor:
                return f'Valor incorreto! Primeiro argumento precisa ser {valor}'
            return funcao(*args, **kwargs)
        return outra
    return interna


@verifica_primeiro_argumento('pizza')
def comida_favorita(*args):
    print(args)


@verifica_primeiro_argumento(10)
def soma_dez(num1, num2):
    return num1 + num2


# Testando
print(soma_dez(10, 12))
print(soma_dez(12, 10))
print(comida_favorita('pizza', 'churrasco'))
print(comida_favorita('sanduiche', 'pizza'))
