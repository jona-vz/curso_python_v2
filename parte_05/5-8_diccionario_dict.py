#tipo de dato compuesto: diccionario

#1.-Creacion de diccionarios:
dic_1 ={'propiedad1': 1, 'propiedad2': 2, 'propiedad3': [1,2,3] }

dic_2 = dict()
dic_2['propiedad1'] = 1
dic_2['propiedad2'] = 2
dic_2['propiedad3'] = [1,2,3]

print(dic_1)
print(type(dic_1))
print()
print(dic_2)
print(type(dic_2))

print()
computador = {'id': 1001, 'marca': 'MSi', 'RAM': 128, 'cpu': 'Intel Core i7 Extreme Edition', 'almacenamiento': 8}
print (computador)
print(f'la variable diccionarion computador tiene {len(computador)} propiedades')
print(type(computador).__name__)

print()
#2.- Acesso a las propiedades  y valores de un diccionario
print('Acesso a las propiedades  y valores de un diccionario')
print(f"ID: {computador['id']}")
print(f"Marca: {computador['marca']}")
print(f"RAM: {computador['RAM']}")
print(f"CPU: {computador['cpu']}")
print(f"Almacenamiento: {computador['almacenamiento']}")

print('cantidad de propiedades del diccionario ´computador´ ', len(computador))

print()
print(computador.get('Almacenamiento', '1'))
print(computador.get('Tarjeta_gráfica', 'integrada'))

print()
#3.- modificacion del contenido de un diccionario
computador['marca'] = 'Alienware'
computador['id'] = 2001
computador['gpu'] = 'NVIDIA GeForce TRX 2081 8gb'


print(f"ID: {computador['id']}")
print(f"Marca: {computador['marca']}")
print(f"RAM: {computador['RAM']}")
print(f"CPU: {computador['cpu']}")
print(f"Almacenamiento: {computador['almacenamiento']}")
print(f"GPU: {computador['gpu']}")

print('cantidad de propiedades del diccionario ´computador´ ', len(computador))

print()
#3.-Itecion de un diccionario
print('Itecion de un diccionario')
#3.1-Itecion de un diccionario por las llaves
print('Itecion de un diccionario por llaves:')

for k in computador.keys():
    print(f'{k.upper()}: {computador[k]}')


print()
#3.2-Itecion de un diccionario por los valores
print('Itecion de un diccionario por los valores:')

for v in computador.values():
    print(v)


print()
#3.3-Itecion de un diccionario por las llaves y los valores
print('Itecion de un diccionario por las llaves y los valores:')

for k, v in computador.items():
    print(f'{k.upper()}: {v}')


print()
#3.4.- metodos y operadores para variables de tipo diccionario
#3.4.1- list(): para covertir las llaves de n diccionario en una lista
print('3.4.1- list(): para covertir las llaves de n diccionario en una lista')
keys = list(computador)
print(keys)
print('cantidad de llaves del diccionario ´computador´', len(keys), len (computador))

#3.4.2- in: para consultar si una llave se encuntra en el diccionario
print('3.4.2- in: para consultar si una llave se encuntra en el diccionario')
print('board' in computador)
print('gpu' in computador)

print()
#3.4.3- pop(): Extrae un elemento del diccionario
print('3.4.3- pop(): Extrae un elemento del diccionario')
#computador.pop('diskette') #genera key error la variable no existe
valor = computador.pop('gpu')
print('Se ha removido la llave ´gpu´del diccionario')
print('el valor de la llave era:', valor) 
print('gpu' in computador)

print()
valor = computador.pop('gpu', 'dispositivo no presente')
print(valor)


print()
#3.4.4- popitem(): Extrae un elemento llave valor del diccionario
print('3.4.3- pop(): Extrae un elemento llave valor del diccionario')
print(computador)

atributo =  computador.popitem()
print(atributo)
print(type(atributo))
print('Llave: ', atributo[0])
print('Valor: ', atributo[1])


print()
#3.4.5- reversed(): invierte el orden de las lllaves del diccionario
print('3.4.5- reversed(): invierte el orden de las lllaves del diccionario')
print(list(computador))
print(list(reversed(computador)))

for k in computador:
    print(f'{k.upper()}: {computador[k]}')

for k in reversed(computador):
    print(f'{k.upper()}: {computador[k]}')

print()
#3.4.6- clear(): remueve todos los eloementos de un diccionario
print('3.4.6- clear(): remueve todos los eloementos de un diccionario')

print(len(computador))
computador.clear()
print(len(computador))