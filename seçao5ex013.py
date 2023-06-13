"""
Média ponderada exemplo:
media = ((nota1 * peso1) + (nota2 * peso2) + (nota3 * peso3)) / (peso1 + peso2 + peso3)
"""


numerador = 0
denominador = 0
n = int(input('Quantidade de NOTAS: '))
for i in range(n):
    nota = float(input(f'\033[32mQual a nota da {i + 1}ª PROVA?\033[m'))
    peso = int(input(f'Qual o PESO da {i +1}ª prova? '))
    numerador = numerador + (nota * peso)
    denominador = denominador + peso
media = numerador / denominador
resultado = media * 10
print('========== RESULTADO ==========')
if resultado >= 60:
    print(f'Com {resultado} pontos o aluno foi \033[34mAPROVADO.\033[m')
elif 50.00 <= resultado <= 59.99:
    print(f'Com {resultado} pontos aluno em \033[33mRECUPRAÇÃO.\033[m')
elif resultado < 50:
    print(f'O aluno com {resultado} pontos está \033[31mREPROVADO\033[m')
