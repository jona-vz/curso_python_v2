#Ejercicio 8.4. Dada la recta y = 6x + 10, comprobar si un punto dado pertenece a ella.


x = int(input("X: "))
y = int(input("Y: "))
print (x, y)

resultado = 6*x + 10
print(resultado)

if resultado == y : 
    print('el punto ({},{}) pertenece a la recta y = 6x + 10 '.format(x, y))
else:
    print('el punto ({},{}) NO pertenece a la recta y = 6x + 10'.format(x, y))

'''
# Ejercicio 8.4. Dada la recta y = 6x + 10, comprobar si un punto dado pertenece a ella.

x = float(input('Escriba el valor de x: '))
y = float(input('Escriba el valor de y: '))

valor = 6 * x + 10

if valor == y:
    print('El punto ({}, {}) se halla en la recta y = 6x + 10'.format(x, y))
else:
    print('El punto ({}, {}) no se halla en la recta y = 6x + 10'.format(x, y))

'''
