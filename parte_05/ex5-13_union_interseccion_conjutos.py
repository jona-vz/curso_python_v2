#Ejercicio 5.13: Realizar operaciones de unión e intersección de conjuntos.

nombres_j = {'juan', 'jorge', 'jona', 'javier', 'joaquin', 'jose', 'josue', 'jonh'}
apellidos_j = {'jimenez', 'jose', 'juarez', 'jacinto', 'jordan', 'jonh', 'jaramillo'}


todos_j = nombres_j.union(apellidos_j)
losdos_j = nombres_j.intersection(apellidos_j)


print('Los nombres y apellidos con j:', todos_j)
print('Los nombres que tambien se pueden usar como apellido son:', losdos_j)

'''
# Ejercicio 5.13: Realizar operaciones de unión e intersección de conjuntos.

numeros = set(list(range(1, 11)))
primos = set([2, 3, 5, 7, 11, 13, 17, 19])

print('Contenido del conjunto `numeros`:', numeros)
print('Contenido del conjunto `primos`:', primos)

print()

union = numeros.union(primos)
print('Contenido del conjunto `union`:', union)
print('Cantidad de elementos del conjunto `union`:', len(union))

print()

interseccion = primos.intersection(numeros)
print('Contenido del conjunto `interseccion`:', interseccion)
print('Cantidad de elementos del conjunto `interseccion`:', len(interseccion))
'''