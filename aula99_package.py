# from sys import path
# # from aula99_package.modulo import soma_do_modulo #1
# import aula99_package.modulo #2
# from aula99_package import modulo #3
# from aula99_package.modulo import * #4
# # print(*path, sep='\n')
# # print(__name__)
# print(soma_do_modulo(1, 2)) #1
# print(aula99_package.modulo.soma_do_modulo(1, 2)) #2
# print(modulo.soma_do_modulo(1, 2)) #2
# print(variavel)
# print(nova_variavel)
# from aula99_package.modulo import soma_do_modulo, fala_oi

# print(__name__)
# fala_oi()
# import aula99_package
from aula99_package import soma_do_modulo, fala_oi

# print(aula99_package.soma_do_modulo(1, 2))
print(soma_do_modulo(1, 2))
fala_oi()