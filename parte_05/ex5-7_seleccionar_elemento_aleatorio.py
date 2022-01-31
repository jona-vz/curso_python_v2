#Ejercicio 5.7: Seleccionar de forma aleatoria un elemento de una lista.

lenguajes = ['python', 'c++', 'javascript', 'c#', 'visual', 'PHP', 'Visual Basic']
print(type(lenguajes))

lenguajes_set = set(lenguajes)
print(type(lenguajes_set))

elemento = lenguajes_set.pop()
print(elemento)

'''
# Ejercicio 5.7: Seleccionar de forma aleatoria un elemento de una lista.

import random

numeros = list(range(1, 7))

numero = random.choice(numeros)

print('Se ha seleccionado de forma aleatoria el valor:', numero)
'''