print('>>>>>> MONTE SEU TRIÂNGULO <<<<<')
lado1 = float(input('Medida do lado "A": '))
lado2 = float(input('Medida do lado "B": '))
lado3 = float(input('Medida do lado "c": '))
if lado1 + lado2 > lado3 and lado3 + lado2 > lado1 and lado1 + lado3 > lado2:
    if lado1 == lado2 == lado3:
        print(f'O trângulo com todos os lados iguais {lado1} é chamado equilatero.')
    elif lado1 == lado2 or lado2 == lado3 or lado3 == lado1:
        print(f'O triângulo com o lado "A" {lado1}, lado "B" {lado2} e lado "C" {lado3} sendo dois iguais e um '
              f'diferente é chamado de equilátero')
    elif lado1 != lado2 != lado3:
        print(f'O triângulo com lado"A" {lado1}, lado"B" {lado2} e lado"C" {lado3}, ou seja todos os lados diferente'
              f' é um triângulo escaleno')
else:
    print(f'Estas medidas não permitem a construção de um triângulo.')
