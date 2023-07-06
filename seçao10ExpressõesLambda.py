"""
Conhecidas por expressões lambda, ou simplesmente lambdas, são funções sem nome ou funções anônimas.nome_completo=lambda, sobrenome:
Ex01
calc = lambda x: 3 * x + 1
print(calc(4)) => 13
print(calc(7)) => 22

Podemos ter expressões lambda com multiplas entradas:
ex01
nome_completo = lambda nome, sobrenome: nome.strip().title() + ' ' + sobrenome.strip().title()

print(nome_completo('   Angelina', 'JOLIE'))

EX02
nome_completo = lambda nome, sobrenome: nome.strip().title() + ' ' + sobrenome.strip().title()

print(nome_completo('ROBSON ', 'vANDER')) => Robson Vander

Em funções python podemos ter nenhuma ou várias entradas, assim é com lambdas.

ex03
ama = lambda: 'Como não amar Python'
uma = lambda x: 3 * x + 1
duas = lambda x, y: (x * y) ** 0.5
tres = lambda x,y,z: 3 /(1/x + 1/ y+1/z)


print(ama())  => Como não amar Python
print(uma(6))  => 19
print(duas(5, 7))  => 5.916079783099616
print(tres(3, 6, 9)) => 4.909090909090908

Obs. Se passarmos mais argumentos do que parâmetros esperados teremos um TypeError

ex04
Outra forma de aplicação lambda.

autores = ['Isaac Asimov', 'Ray Bradburry', 'Robert Heinlein', 'Arthur C. Clarke',
           'Frank Hebert', 'Orson Scott Cord', 'Douglas Adam', 'H. G. Wells', 'Leigh Brackey']

print(autores) #Sem aplicar a ordenação
=> ['Isaac Asimov', 'Ray Bradburry', 'Robert Heinlein', 'Arthur C. Clarke', 'Frank Hebert',
 'Orson Scott Cord', 'Douglas Adam', 'H. G. Wells', 'Leigh Brackey']

autores.sort(key=lambda sobrenome: sobrenome.split(' ')[-1].lower())

print(autores) #Aplicando a ordena pelo sobrenome
=>  ['Douglas Adam', 'Isaac Asimov', 'Leigh Brackey', 'Ray Bradburry', 'Arthur C. Clarke', 'Orson Scott Cord',
'Frank Hebert', 'Robert Heinlein', 'H. G. Wells']

ex05
Aplicando lambda dentro de funções:
função quadrática => Exemplo => f(x) = a * x ** 2 + b * x + c

def gerador_função_quadratica(a, b, c):
    '''
    Retorna uma função quadrática.
    :param a: parâmetros informados
    :param b: parâmetros informados
    :param c: parâmetros informados
    :return: x: a * x ** 2 + b * x + c
    '''
    return lambda x: a * x ** 2 + b * x + c


teste = gerador_função_quadratica(2, 3, -5)

print(teste(0)) => -5
print(teste(1)) => 0
print(teste(2)) => 9

Obs.: Não há necessidade de criar uma variável, pode-se passar lambda dentro da função.
"""
print('Fim desta aula 04/07/23')
