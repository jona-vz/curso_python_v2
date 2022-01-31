#Ejercicio 5.8: Calcular la frecuencia (ocurrencias) de los elementos de una lista.

numeros =[1,2,3,4,5,5,4,2,2,3,4,5]
numeros_unicos = []

for i, v in enumerate(numeros):
    if v not in numeros_unicos:
        numeros_unicos.append(v)
     
for i in numeros_unicos:
    veces = numeros.count(i)
    print(f'El {i} aparece {veces} veces en las lista')


'''
# Ejercicio 5.8: Calcular la frecuencia (ocurrencias) de los elementos de una lista.

from collections import Counter

numeros = [1, 2, 3, 1, 1, 1, 4, 5, 6, 3, 3, 2, 5]
print('Contenido actual de la lista `numeros`:', numeros)
print('Cantidad actual de elementos de la lista `numeros`:', len(numeros))

print()

# Solución #1:
print('Solución #1')

frecuencia = {}

for n in numeros:
    if n in frecuencia:
        frecuencia[n] += 1
    else:
        frecuencia[n] = 1

print('Contenido actual del diccionario `frecuencia`:', frecuencia)
print('Cantidad actual de elementos del diccionario `frecuencia`:', len(frecuencia))

print()

# Solución #2:
print('Solución #2')

contador = Counter(numeros)
print('Contenido actual de la variable `contador`:', contador)

'''