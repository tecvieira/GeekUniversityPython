"""
A idéia de herança é o reaproveitamento de códigos. Também extender nossas classes.
Obs,: Com a herança, a partir de uma classe existente, nos estendemos outra classe que
passa a herdar atributos e métodos da classe herdada
obs2. Quando uma classe herda de outra classe ela recebe Todos os atributos e métodos da classe herdada.

Obs 3 - A classe herdada passa ser reconhecida como:
=== Nomenclaturas Utilizadas===
- super Classe;
- classe Mãe
- classe Pai
- classe Base
- classe Genérica

Obs 4 - Quando uma classe herda de outtra ela é chamada de :
- sub Classe
- classe Filha
- classe Específica

Textando:
print(cliente1.nome_completo())
print(funcionario1.nome_completo())

saídas:
 Angelina Jolie
 Felicity Jones
{'_Pessoa__nome': 'Angelina', '_Pessoa__sobrenome': 'Jolie', '_Pessoa__cpf':'123.456.789-00', '_Cliente__renda': 5000}
{'_Pessoa__nome': 'Felicity', '_Pessoa__sobrenome': 'Jones','_Pessoa__cpf': '987.654.321.-11',
'_Funcionarios__matricula': 1234}
"""


class Pessoa:
    def __init__(self, nome, sobrenome, cpf):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'


class Cliente(Pessoa):
    def __init__(self, nome, sobrenome, cpf, renda):
        super().__init__(nome, sobrenome, cpf)
        self.__renda = renda


class Funcionarios(Pessoa):
    def __init__(self, nome, sobrenome, cpf, matricula):
        super().__init__(nome, sobrenome, cpf)
        self.__matricula = matricula


cliente1 = Cliente('Angelina', 'Jolie', '123.456.789-00', 5000)
funcionario1 = Funcionarios('Felicity', 'Jones', '987.654.321.-11', 1234)

print(cliente1.nome_completo())
print(funcionario1.nome_completo())

print(cliente1.__dict__)
print(funcionario1.__dict__)
