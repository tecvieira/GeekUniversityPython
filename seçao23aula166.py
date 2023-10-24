"""
Tipos de dados mais precisos:
def dobro(valor: int) -> int:
    return valor * 2


print(dobro(8))
print(dobro('geek')) => Mesmo sendo executado o mypy apresenta erro pois não é o tipo de dado experado.
verifique com a ferramenta mypy no terminal

error: Argument 1 to "dobro" has incompatible type "str"; expected "int"  [arg-type]
Found 1 error in 1 file (checked 1 source file)

from typing import Literal

def pegar_status(usuário: str) -> Literal['conectado', 'desconectado']:
    pass
# o valor deverá ser uma string porém o retorno será do tipo conectado ou desconectado, ao implementar a
função devemos observar esta necessidade.
____________________________________________________________________
def calcula_v1(operacao: str,
               num1: int,
               num2: int, ) -> None:
    if operacao == '+':
        print(f'{num1} + {num2} = {num1 + num2}')
    elif operacao == '-':
        print(f'{num1} - {num2} = {num1 - num2}')
    else:
        raise ValueError(f'operação Inválida {operacao!r}')


calcula_v1('+', 6, 4) => 6 + 4 = 10
calcula_v1('-', 10, 2) => 10 - 2 = 8
calcula_v1('*', 3, 5) => ValueError: operação Inválida '*'

_____________________________________________________________________
Ex.2
from typing import Literal


def calcula_v2(operacao: Literal['+', '-'],
               num1: int,
               num2: int, ) -> None:
    if operacao == '+':
        print(f'{num1} + {num2} = {num1 + num2}')
    elif operacao == '-':
        print(f'{num1} - {num2} = {num1 - num2}')
    else:
        raise ValueError(f'operação Inválida {operacao!r}')

# !r vai indicar o tipo de erro


calcula_v2('+', 6, 4) => 6 = 4 = 10
calcula_v2('-', 10, 2) => 10 - 2 = 8
calcula_v2('*', 3, 5) => ValueError: operação Inválida '*'
____________________________________________________________________
from typing import Union


def soma(num1: int, num2: int) -> Union[str, int]:
    resultado: int = num1 + num2
    if resultado > 50:
        return f'O valor {resultado} é muito grande'
    else:
        return resultado


print(soma(6, 4))
print(soma(10, 2))
print(soma(30, 25))
_____________________________________________________________________
from typing import final


@final
class Pessoa:
    pass


class Estudante(Pessoa): #erro no mypy
    pass

    @final
    def estudar(self):
        print('Estou estudando')

class Estagiario(Estudante):
    pass

    def estudar(self):
        print('Eestudante e estagiário')

#Erros do mypy:
Usando o @final não é possivel extender uma class para classe filha ou para um método

seçao23aula166.py:83: error: Cannot inherit from final class "Pessoa"  [misc]
seçao23aula166.py:90: error: Cannot inherit from final class "Pessoa"  [misc]
Found 2 errors in 1 file (checked 1 source file)
______________________________________________________________________________________
from typing import TypedDict


class CursoPython(TypedDict):
    versao: str
    atualizacao: int


geek = CursoPython(versao='3.8.5', atualizacao=2020)
print(geek) => {'versao': '3.8.5', 'atualizacao': 2020}

outro = CursoPython(algo='vai', coisa=True)
print(outro)

 => {'algo': 'vai', 'coisa': True}
#Erro mypy:
seçao23aula166.py:113: error: Missing keys ("versao", "atualizacao") for TypedDict "CursoPython"  [typeddict-item]
seçao23aula166.py:113: error: Extra keys ("algo", "coisa") for TypedDict "CursoPython"  [typeddict-unknown-key]
Found 2 errors in 1 file (checked 1 source file)
_____________________________________________________________________________________________________

"""
from typing import Protocol


class Curso(Protocol):
    titulo: str

def estudar(valor: Curso) -> None:
    print(f'Estou estudando o curso {valor: titulo}')


class Venda:
    titulo= 'oi'

v1 = Venda()
estudar(v1)

#Um protolo é como uma regra a seguir.
#O tipo ou objeto é menos importante que suas caracteristicas desde que siga o protolo.
# Este código não executa pois não foi definido o protolo
# confesso que não entendi este assunto!!!!
