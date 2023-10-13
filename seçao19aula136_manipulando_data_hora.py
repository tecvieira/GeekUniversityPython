"""
Python tem um módulo built-in (integrado) para se trabalhar com data e hora chamado datetime.
# importando a módulo

import datetime
 dentro deste módulo existe a classe também com mesmo nome.

 Ex.
 print(datetime.datetime.now())
 => 2023-09-30 14:36:18.503280

 # verificando a representação.
 print(repr(datetime.datetime.now))
 <built-in method now of type object at 0x7f27d94f88e0>

 Ajustando data e hora programada
 inicio = datetime.datetime.now()
 => 2023-09-30 19:17:02.204430
 inicio = inicio.replace(hour=21, minute=0, second=0, microsecond=0)
 => 2023-09-30 21:00:00

 Obs.: Pode-se aplicar também a data.

 Imprimindo um evento programado:
 evento = datetime.datetime(2023, 9, 29, 0)
print(evento) => 2023-09-29 00:00:00

 Recebendo uma data do usuário:

 evento = input('Informe sua data de aniversário: DD/MM/AAAA ')
aniversario = evento.split('/')
aniversario = datetime.datetime(int(aniversario[2]), int(aniversario[1]), int(aniversario[0]))
print(aniversario)  => 2004-09-02 00:00:00

Podemos ter acesso individual de data e hora
evento = datetime.datetime.now()
print(evento.year)
print(evento.month)
print(evento.hour)
print(evento.minute)
=> 2023
=> 10
=> 15
=> 57

"""
import datetime


evento = datetime.datetime.now()
print(evento.year)
print(evento.month)
print(evento.hour)
print(evento.minute)


