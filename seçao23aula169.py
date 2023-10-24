"""
Metadata (meta dados internos, novidades da versão 3.8 do Python
from importlib import metadata

print(metadata.version('pip'))
=> 22.3.1
_________________________________________________________________
Mostrando os metadados existente nesta versão do pip.

from importlib import metadata

metadados_pip = metadata.metadata('pip')
=> ['Metadata-Version', 'Name', 'Version', 'Summary', 'Home-page', 'Author',
'Author-email', 'License', 'Project-URL', 'Project-URL', 'Project-URL', 'Classifier',
'Classifier', 'Classifier', 'Classifier', 'Classifier', 'Classifier', 'Classifier',
'Classifier', 'Classifier', 'Classifier', 'Classifier', 'Classifier',
'Classifier', 'Classifier', 'Requires-Python', 'License-File', 'Description']
_________________________________________________________________________________________
from importlib import metadata

print(metadata.requires('django'))
=> ['asgiref <4,>=3.6.0', 'sqlparse >=0.3.1', 'backports.zoneinfo ; python_version < "3.9"', 'tzdata ;
 sys_platform == "win32"', "argon2-cffi >=19.1.0 ; extra == 'argon2'", "bcrypt ; extra == 'bcrypt'"]


"""
from importlib import metadata

print(metadata.requires('django'))
