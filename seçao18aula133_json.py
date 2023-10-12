"""
JSON => JavaScript object notation
API => Normalmente utilizado em arquivos de API, que são meios de comunicação entre os serviços oferecidos por empresas
(Twitter, Facebook, Youtube
"""
import json


ret = json.dumps(['produto', {'Playstation 4': ('2TB', 'NOVO', '220V', 2340)}])
print(type(ret))
print(ret)
