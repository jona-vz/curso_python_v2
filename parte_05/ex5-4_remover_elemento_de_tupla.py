#Ejercicio 5.4: Remover un elemento (valor) de una tupla.


pares = (2,4,6,8,10,12,14,16,18,20)
print(pares)
pares = list(pares)
print(pares)

numero_removido = pares.pop()
print(pares)
print(numero_removido)

pares = tuple(pares)
print(pares)
print(numero_removido)


'''
# Ejercicio 5.4: Remover un elemento (valor) de una tupla.

lenguajes = ('Python', 'JavaScript', 'Perl', 'C++', 'Java')
print('Contenido actual de la tupla `lenguajes`:', lenguajes)
print('Cantidad de elementos de la tupla `lenguajes`:', len(lenguajes))

lenguaje = 'Perl'

if lenguaje in lenguajes:
    
    # NOTA IMPORTANTE: Las tuplas no se pueden modificar. Las tuplas son inmutables.
    lenguajes = lenguajes[0:2] + lenguajes[3:]

    print()

    print('Contenido actual de la tupla `lenguajes`:', lenguajes)
    print('Cantidad de elementos de la tupla `lenguajes`:', len(lenguajes))

else:
    print('No existe un nombre de lenguaje con:', lenguaje)

'''