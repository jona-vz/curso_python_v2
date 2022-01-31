#ciclos - for

numeros = [1, 2, 3, 4, 5]

total = 0

total = numeros[0] + numeros[1] + numeros[2] + numeros[3] + numeros[4]
print('Total de la suma de los nuemeros del 1 al 5:', total)


total = 0
total += numeros[0]
total += numeros[1]
total += numeros[2]
total += numeros[3]
total += numeros[4]
#total += numeros[999]
print('Total de la suma de los nuemeros del 1 al 5:', total)

numeros.append(6)
numeros.append(7)
numeros.append(8)
numeros.append(9)
numeros.append(10)

print('Contenido actual d la lista ´numeros´:', numeros)

total += numeros[5]
total += numeros[6]
total += numeros[7]
total += numeros[8]
total += numeros[9]
#total += numeros[999]
print('Total de la suma de los nuemeros del 1 al 10:', total)

print()

#Uso explicito del ciclo for para resolver un prblema que requiere 
#iterar (recorrer) todos los elementos de una coleccion (lista):

total = 0

for i in range(0, len(numeros)):
    total  += numeros[i]

print('Total de la suma de los nuemeros del 1 al 10:', total)

print()

#suma de los numeros paers que hay en la lista ´numeros´:
print('suma de los numeros paers que hay en la lista ´numeros´:')

suma_pares = 0

for i in range(len(numeros)):
    if numeros[i]%2 == 0 :
        suma_pares += numeros[i]

print('La suma de los numeros pares en la lista numeros es igual a ', suma_pares)

print()

#suma de los numeros impares que hay en la lista ´numeros´:
print('suma de los numeros impares que hay en la lista ´numeros´:')

suma_impares = 0
for i in range(len(numeros)):
    if numeros[i]%2 :
        suma_impares += numeros[i]

print('La suma de los numeros impares en la lista numeros es igual a ', suma_impares)

print()

# Iteracion con un ciclo for mejorado - iteracion por los elementos de una coleccion:
print('Iteracion con un ciclo for mejorado - iteracion por los elementos de una coleccion:')

total = 0

for n in numeros:
    print ('El valor de ´n´ es', n)
    total += n

print('Total de la suma de los nuemeros del 1 al 10:', total)

print()

#Suma de los elementos pares de una lista utilizando un ciclo for mejorado: 
print('Suma de los elementos pares de una lista utilizando un ciclo for mejorado: ')

suma_pares = 0

for n in numeros:
    if n%2 == 0:
        suma_pares += n

print('La suma de los numeros pares que hay en la lista numeros es: ', suma_pares)


print()

#Suma de los elementos impares de una lista utilizando un ciclo for mejorado: 
print('Suma de los elementos impares de una lista utilizando un ciclo for mejorado: ')

suma_impares = 0

for n in numeros:
    if n%2 == 1:
        suma_impares += n

print('La suma de los numeros impares que hay en la lista numeros es: ', suma_impares)


print()

#Uso de listas de comprension para simplificar el proceso de suma de elementos de una lista: 
print('Uso de listas de comprension para simplificar el proceso de suma de elementos de una lista: ')

total = [numeros[i] for i in range(len(numeros))]

print('Contenido de la variable total', total)

total = sum([numeros[i] for i in range(len(numeros))])

print('El contenido de total pero ya sumado: ', total)

print()

#Suma de pare e impares usando una lista de comprension: 
print('Suma de pare e impares usando una lista de comprension: ')

pares = [numeros[i] for i in range(len(numeros)) if numeros[i] % 2 == 0]

print('Pares: ', pares)
print('Tipo de dato de pares: ', type(pares))

suma_pares = sum(pares)

print ('La suma de los nuemeros pares es igual a: ', suma_pares)

impares = [numeros[i] for i in range(len(numeros)) if numeros[i] % 2 == 1]

print('Impares: ', impares)
print('Tipo de dato de impares: ', type(impares))

suma_impares = sum(impares)

print ('La suma de los nuemeros impares es igual a: ', suma_impares)


print()

#Uso de la funcion enumerate para realizar una iteracion por indice y valor
print('Uso de la funcion enumerate para realizar una iteracion por indice y valor')

for i, n in enumerate(numeros):
    print('Indice: %i. Valor: %i' % (i, n))
    



