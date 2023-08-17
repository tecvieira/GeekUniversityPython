"""
- Decorators são funções:
- Decorators envolvem outras funções e aprimoram seus comportamentos
- Decorators também são exemplos higher Order Functions
- Decorators tem uma sintaxe própria, usando " @ " (Syntact Sugar / Áçucar Sintático)
Exemplo1 - Sem Áçucar Sintático - Não indicado
"""


def seja_educado_mesmo(funcao): # Decorators Functions
    def sendo_mesmo():
        print('Foi um prazer conhecer voce')
        funcao()
        print('Tenha um ótimo dia!')
    return sendo_mesmo()


def saudacao():
    print('Seja bem vindo a Geek University')


teste = seja_educado_mesmo(saudacao)

teste
