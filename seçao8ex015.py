def forma_triangulo(a, b, c):
    if a < b + c and b < a + c and c < a + b:
        if a == b == c:
            print(f'Com medidas {a}, {b} e {c}, e os tres lados iguais formará um triângulo equilátero.')
        elif a == b or a == c or b == c:
            print(f'Com medidas {a}, {b} e {c}, e dois lados iguais, formara um triângulo isosceles.')
        else:
            print(f'Com medidas {a}, {b} e {c}, e os três lados diferentes formara um triangulo escaleno.')
    else:
        print('Com estas medidas não é possivel formar um triângulo.')


forma_triangulo(a=float(input('Primeira medida: ')), b=float(input('Segunda medida: ')),
                c=float(input('Terceira medida: ')))
