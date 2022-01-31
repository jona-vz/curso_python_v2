#Ejercicio 4. Calcular el área superficial y el volumen de un cilindro.

from math import pi

r = 5
h = 20

area = 2 * pi * r * h + 2 * pi * r ** 2
volumen = pi * r **2 * h

print('Area = ', area)
print('Volumen = ', volumen)

'''
# Ejercicio 4. Calcular el área superficial y el volumen de un cilindro.

from math import pi

radio = float(input('Escriba el radio del cilindro: '))
altura = float(input('Escriba la altura del cilindro: '))

area_superficial = 2 * pi * radio ** 2 + 2 * pi * radio * altura

volumen =  pi * radio **2 * altura

print('El área del cilindro es:', area_superficial)
print('El volumen del cilindro es:', volumen)
'''