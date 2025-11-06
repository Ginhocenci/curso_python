import sys
# Generator expression, Iterables e Iterators em Python
iterable = ['Eu', 'Tenho', '__iter__']
# iterator = iterable.__iter__() # tem __iter__ e __next__
iterator = iter(iterable) # tem __iter__ e __next__
lista = [n for n in range(10000)]
generator = (n for n in range(10000))
print(sys.getsizeof(lista)) # Fica toda na memória, mas é possível buscar um index.
print(sys.getsizeof(generator)) #não tem como saber o tamanho ou acessar um index.

print(next(generator))
print(next(generator))
print(next(generator))

for n in generator:
    print(n)

# print(next(iterator))
