#tipo de dato compuestod inamico y mutablr :SET

#1. creacion de conjunto
print('#1. creacion de conjunto')

conjunto_1 = {'Juan', 'Oliva', ' Edward', 'Daniela', 'Juan', 'Juan', 'German'}
conjunto_2 = set(['Juan', 'Oliva', ' Edward', 'Daniela', 'Juan', 'Juan', 'German'])

print('Contenido de la variaable conjunto_1:  ', conjunto_1)
print('Cantidad de elementos del conjunto_1', len(conjunto_1))
print('El tipo de dato del conjunto_1', type(conjunto_1))
print()
print('Contenido de la variaable conjunto_2:  ', conjunto_2)
print('Cantidad de elementos del conjunto_2', len(conjunto_2))
print('El tipo de dato del conjunto_2', type(conjunto_2))


print()
#1.2 creacion de conjuntos por medio de cadenas de caracteres
print('#1.2 creacion de conjunto medio de cadenas de caracteres')
frase = 'Python es un lenguaje de programación'
caracteres = set(frase)
print('contenido de la variable conjunto ´caracteres´:  ', caracteres)
print('El tipo de dato del conjunto ´caracteres´: ', type(caracteres))
print('Cantidad de elementos del conjunto ´caracteres', len(caracteres))
print('Cantidad de caracteres de ña variable string ´frase´:  ', len(frase))

print()
#1.3 creacion de conjuntos por medio de tuplas
print('#1.3 creacion de conjunto medio de tuplas')

primos = (7,3,5,2,7,5,13,11,19,2,2,2,5,5)
print('contenido de la variable tuple ´primos´:  ', primos)
print('Cantidad de elementos de la tupla ´primos´: ', len(primos))
print('El tipo de dato de la tupla ´primos´: ', type(primos))

print()
primos_unicos = set (primos)
print('contenido de la variable conjunto ´primos_unicos´:  ', primos_unicos)
print('Cantidad de elementos de la conjunto ´primos_unicos´: ', len(primos_unicos))
print('El tipo de dato de la conjunto ´primos_unicos´: ', type(primos_unicos))

print()
#1.4 creacion del conjunto de colores del arcoiris
print('#1.2 creacion de conjunto de colores del arcoiris')

arco_iris = {'Rojo', 'Naranja', 'Amarillo', 'Verde', 'Azul', 'Añil'}

print('contenido de la variable conjunto ´colores´:  ', arco_iris)
print('Cantidad de elementos del conjunto ´colores´: ', len(arco_iris))
print('El tipo de dato del conjunto ´colores´: ', type(arco_iris))


print()
#2. Agregacion de elementos a un conjunto utilizando el metodo add()
print('#2. Agregacion de elementos a un conjunto utilizando el metodo add()')

arco_iris.add('Violeta')
print('contenido de la variable conjunto ´colores´:  ', arco_iris)
print('Cantidad de elementos del conjunto ´colores´: ', len(arco_iris))
print('El tipo de dato del conjunto ´colores´: ', type(arco_iris))
print()
arco_iris.add('Violeta')
arco_iris.add('Violeta')
arco_iris.add('Violeta')
print('contenido de la variable conjunto ´colores´:  ', arco_iris)
print('Cantidad de elementos del conjunto ´colores´: ', len(arco_iris))
print('El tipo de dato del conjunto ´colores´: ', type(arco_iris))


print()
#3. Iteracion de un conjunto
print('#3. Iteracion de un conjunto')

for c in arco_iris:
    print(c)

print()
#3.2 Iteracion de un conjunto con enumarate()
print('#3. Iteracion de un conjunto con enumarate()')

for i, c in enumerate(arco_iris):
    print(f'Indice: {i} - Color: {c}')

#nota: no existe el concepto de orden en un conjunto 


print()
#4. operacion de contencion (o pertenencia) en un conjunto
print('#4. operacion de contencion  (o pertenencia) en un conjunto')

color = 'Gris'
resultado = color in arco_iris
print('¿el color %s se encuntradentro de colores? %s' %(color, resultado))

print()
color = 'Azul'
resultado = color in arco_iris
print('¿el color %s se encuntradentro de colores? %s' %(color, resultado))

print()
color = 'violeta' #distincion en mayusculas y minusculas
resultado = color in arco_iris
print('¿el color %s se encuntradentro de colores? %s' %(color, resultado))

print()
#4.2 operacion de subconjunto
print('#4.2 operacion de subconjunto')

colores = {'Rojo', 'Verde', 'Azul'}
resultado = colores.issubset(arco_iris)
print('¿El conjunto {} es subconjunto de {}?: {}'.format(colores, arco_iris, resultado))
print()
colores.add('Gris')
resultado = colores.issubset(arco_iris)
print('¿El conjunto {} es subconjunto de {}?: {}'.format(colores, arco_iris, resultado))

print()
vacio = set([])
print('Cantidad de elemento del conjunto ´vacio´ : ', len(vacio))

resultado = vacio.issubset(arco_iris)
print('¿El conjunto {} es subconjunto de {}?: {}'.format(vacio, arco_iris, resultado))


print()
#4.3 operacion de union
print('#4.3 operacion de union')
mas_colores = arco_iris.union(colores)

print('contenido de la variable conjunto ´colores´:  ', mas_colores)
print('Cantidad de elementos del conjunto ´colores´: ', len(mas_colores))
print('El tipo de dato del conjunto ´colores´: ', type(mas_colores))

print()
#4.3 operacion de interseccion
print('#4.3 operacion de interseccion')
interseccion = arco_iris.intersection(colores)

print('contenido de la variable conjunto ´colores´:  ', interseccion)
print('Cantidad de elementos del conjunto ´colores´: ', len(interseccion))
print('El tipo de dato del conjunto ´colores´: ', type(interseccion))

print()
#4.4 operacion de super conjunto
print('#4.4 operacion de super conjunto')

rgb = {'Rojo', 'Verde', 'Azul'}
resultado = arco_iris.issuperset(rgb)
print('¿El conjunto {} es superconjunto de {}?:   {}'.format(arco_iris, rgb, resultado))

rgb.add('Gris')
resultado = arco_iris.issuperset(rgb)
print('¿El conjunto {} es superconjunto de {}?:   {}'.format(arco_iris, rgb, resultado))

print()
#4.5 operacion de diferencia de conjuntos
print('#4.5 operacion de diferencia de conjuntos')

# A = {1, 2, 3} 
# B = {3, 4, 5}
# C = A - B = {1, 2}
# D = B - A = {4, 5}

diferencia = colores - arco_iris
print('La diferencia entre los conjuntos ´arcoiris´y ´colores´ es:    ', diferencia)
print()
diferencia = arco_iris - colores
print('La diferencia entre los conjuntos ´colores´y ´gris´ es:    ', diferencia)


print()
#4.6 operacion de diferencia simetrcia entre dos conjuntos
print('#4.6 operacion de diferencia simetrcia entre dos conjuntos')

dif_simetrica = arco_iris.symmetric_difference(colores)
print('La diferencia simetrica entre los conjuntos arcoiris y colores es: ', dif_simetrica)

print()
#5. otras operaciones
#5.1 método remove()
print('#5.1 método remove()')

print('contenido de la variable conjunto ´colores´:  ', colores)
print('Cantidad de elementos del conjunto ´colores´: ', len(colores))
print('El tipo de dato del conjunto ´colores´: ', type(colores))
colores.remove('Gris') #si se le pone 'gris' marca error
print()

print('contenido de la variable conjunto ´colores´:  ', colores)
print('Cantidad de elementos del conjunto ´colores´: ', len(colores))
print('El tipo de dato del conjunto ´colores´: ', type(colores))

print()
#5.2 método pop()
print('#5.2 método pop()')
print('contenido de la variable conjunto ´colores´:  ', colores)
print('Cantidad de elementos del conjunto ´colores´: ', len(colores))
print('El tipo de dato del conjunto ´colores´: ', type(colores))

color = colores.pop()
print()

print('contenido de la variable conjunto ´colores´:  ', colores)
print('Cantidad de elementos del conjunto ´colores´: ', len(colores))
print('El tipo de dato del conjunto ´colores´: ', type(colores))

print('El color que se removió del conjunto ´colores´: ' , color)

print()
#5.3 método clear()
print('#5.3 método clear()')

print()

print('contenido de la variable conjunto ´colores´:  ', colores)
print('Cantidad de elementos del conjunto ´colores´: ', len(colores))
print('El tipo de dato del conjunto ´colores´: ', type(colores))

colores.clear()

print()

print('contenido de la variable conjunto ´colores´:  ', colores)
print('Cantidad de elementos del conjunto ´colores´: ', len(colores))
print('El tipo de dato del conjunto ´colores´: ', type(colores))