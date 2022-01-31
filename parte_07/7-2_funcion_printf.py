#salida de datos (ouput) -Funcion print():
print('salida de datos (ouput) -Funcion print():')

nombre = 'Jonathan Vasquez Alvarado'
edad = 26

print('Nombre: ' + nombre, end=' - ')
print('Edad: ' + str(edad))


print('Aprendiendo el uso de la', end=' ')
print('funcion print()')

print()
#Multiples argumentos de la funcion print()'
print('Multiples argumentos de la funcion print()')

email = 'jona@gmail.com'

print(nombre, edad, email)

print(nombre, edad, email, sep=' - ')

print()

lenguajes = ('python', 'js', 'C++', 'C#', 'Java')

print(lenguajes)
print(lenguajes[0], lenguajes[1], lenguajes[2], lenguajes[3], lenguajes[4], sep=' - ')

print()
#Expansion (desempaquetamiento) de una coleccion:
print('Expansion (desempaquetamiento) de una coleccion:')

print(*lenguajes, sep=' - ')