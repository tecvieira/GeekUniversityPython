"""
Manipulando data e hora:
print(datetime.datetime.now()) # mostra hora e data atual  => 2023  -09    -22  10    :07      :02     .942157
                                                              year, month, day, hour, minute, seconds, microsecond
print(datetime.MAXYEAR) => 9999 # ano máximo permitido
print(datetime.MINYEAR) => 1 # menor ano permitido
print(repr(datetime.datetime.now())) => datetime.datetime(2023, 9, 22, 10, 7, 2, 942221) #representação da data atual

# criando um evento futuro/ determinando uma data:
evento = datetime.datetime(2023, 10, 10, 0)
print(evento) =>2023-10-10 00:00:00

#Acesso individual de data e hora:
"""
import datetime


print(datetime.datetime.now())
print(datetime.MAXYEAR)
print(datetime.MINYEAR)
print(repr(datetime.datetime.now()))
evento = datetime.datetime(2023, 10, 10, 0)
print(evento)
print(evento.year)
print(evento.month)
print(evento.day)
print(evento.hour)
print(evento.minute)
print(evento.second)

