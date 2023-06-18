def convert_segundos(h, m, s):
    hora = ((h * 3600) + (m * 60) + s)
    print(f'O horário de {h}h{m}m{s}s corresponde a {hora} segundos.')


convert_segundos(h=int(input('Quantas horas: ')), m=int(input('Quantos minutos: ')), s=int(input('Quantos segundos: ')))
