print('\033[33m========= CALCULE ÁREA DO TRAPÉZIO ==========')
altura = 0
areatrapezio = 0
basemaior = float(input('Informe o tamanho da base maior: '))
basemenor = float(input('Informe o tamanho da base menor: \033[m'))
if basemaior and basemenor > 0:
    altura = float(input('Informe altura do trapézio: '))
    areatrapezio  = ((basemaior + basemenor) * altura) / 2
else:
    print('\033[31mValores indevidos para o cálculo: ')


print(f'O trapézio com medidas: {basemaior} de base maior, {basemenor} de base menor'
      f' e {altura} altura tem área de {areatrapezio} (unidade)²')
