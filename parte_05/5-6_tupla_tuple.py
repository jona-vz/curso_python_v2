#tipo de dato compuesto - tupla - estático

punto = (2,5)
print(type(punto))
print(punto)
print(len(punto))

#acceso a los elementos de una tupla
print()
x = punto[0]
y = punto[1]
print ('el valor de la variable x es: ', x)
print ('el valor de la variable y es: ', y)

print()
#desempaquetamiento
abscisa, ordenada = punto
print ('el valor de la variable abscisa es: ', abscisa)
print ('el valor de la variable ordenada es: ', ordenada)


print()
#acceso con indices negativos
ultimo_elemento = punto[-1]
penultimo_elemento = punto[-2]
print ('el valor de la variable ultima es: ', ultimo_elemento)
print ('el valor de la variable penultima es: ', penultimo_elemento)


print ()
#concepto de inmutabilidad en una variable
#punto[0] = 3 #type error

punto = (3, 7)
x = punto[0]
y = punto[1]
print ('el valor de la variable x es: ', x)
print ('el valor de la variable y es: ', y)

print()
#iteacion de un objeto tupla (tuple)

numeros_primos = (2,3,5,7,11,13,17,19)
print(type(numeros_primos))
print('Cantidad de elementos en numeros_primos', len(numeros_primos))



#iteracion con while
print('iteracion en el ciclo while ')
i=0
while i < len(numeros_primos):
    print(f'el valor del elemento en el indice {i} es igual a {numeros_primos[i]}.') 
    i = i+1

print()
#iteracion con for
print('iteracion en el ciclo for')
for i in range(len(numeros_primos)) :
    print(f'el valor del elemento en el indice {i} es igual a {numeros_primos[i]}.') 

print()
#iteracion con for mejorado
print('iteracion en el ciclo for mejorado')
for p in numeros_primos :
    print('Valor', p)

print()
#iteracion de una tupla con la funcion enumerate()
print('iteracion en la funcion enumerate')
for i, v in enumerate(numeros_primos):
    print(f'el valor del elemento en el indice {i} es igual a {v}.') 


print()
#Mecanismos alternativos para crear una tupla
#Modo A:
numeros = 1,2,3
print(type(numeros))
print(numeros)
print(len(numeros))

numeros = 1,
print(type(numeros))
print(numeros)
print(len(numeros))

print()
#Modo B: uso de la clase tuple()
numeros = tuple([1,2,3])
print(type(numeros))
print(numeros)
print(len(numeros))

print()
#operaciones básicas que provee la clase tuple()
print('operaciones básicas que provee la clase tuple()')
colores = ('negro', 'blanco', 'negro', 'azul', 'negro', 'rojo', 'verde')
print (colores.count('negro'))
print (colores.count('Negro'))#distingue entre mayus y minus
print (colores.index('rojo'))
print (colores.index('negro'))