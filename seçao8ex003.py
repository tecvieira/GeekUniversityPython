def testaSinal():
    numero = int(input('Informe um número: '))
    if numero > 0:
        print(1)
    elif numero < 0:
        print(-1)
    elif numero == 0:
        print(0)


print(f'O valor abaixo indica:')
testaSinal()
print(""" 
 1 - número positivo
-1 - número negativo
 0 - valor zero
""")