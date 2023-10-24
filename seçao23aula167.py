"""
Fstrings: de
Com o novo recurso adicionado ao fstrings facilmente podemos debugar valores ou expressões bastando adicionar
o nome da variável juntamente com sinal de igual.
_____________________________________________________________________
def multiplicar(num1: float, num2: float) -> float:
    return num1 * num2


resultado: float = multiplicar(4.2345, 6.7890)
print(f'O resultado é {resultado}')

=> O resultado é 28.748020499999996
___________________________________________________________________
Outra forma Ex2:
print(f'O resultado é {multiplicar(9, 4):.2f}')
=> O resultado é 36.00
___________________________________________________________________
Utilizando o operador walrus:
print(f'{(media := 8/2)} é a metade de {media * 2}')
=> 4.0 é a metade de 8.0
___________________________________________________________________
Aplicando novo recurso:
geek: str = "Geek University"
print(f"geek= '{geek}'")
=> geek= 'Geek University'
___________________________________________________________________
Com novo recurso:
geek: str = "Geek University"
print(f'{geek=}')
=> geek= 'Geek University'
__________________________________________________________________
Fazendo algo mais complexo:
geek: str = "Geek University"
print(f'{geek.upper()[ :: -1] = }')
=> geek.upper()[ :: -1] = 'YTISREVINU KEEG'


"""
geek: str = "Geek University"
print(f'{geek.upper()[ :: -1] = }')
