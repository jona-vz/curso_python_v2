#numeros de punto flotante  
pi =3.1416
precio = 29.95

print('El valor de la variable pi es:  %.4f' %pi)
print('El valor de la variable precio es:  %.2f' %precio)
print(pi)
print(precio)

print('El tipo de dato de la variable pi es:  %s' %type(pi))
print('El tipo de dato de la variable precio es:  %s' %type(precio))

print()
print('OPERACIONES ARITMETICAS SOBRE NUMEROS DE PUNTO FLOTANTE')

pi = pi * 2
print('el nuevo valor de pi es: ', pi)

total = precio * 5
print('El total de la compra es: %.2f' % total)

print('El tipo de dato de la variable pi es:  %s' %type(pi))
print('El tipo de dato de la variable total es:  %s' %type(precio))

print()
print('CREACION DE UN NUMERO REAL A PARTIR DE UNA CADENA DE CARACTERES')

precio_compu = float(input('dame el precio de la computadora'))
print('El tipo de dato de la variable precio_compu es:  %s' %type(precio_compu))
print('La computadora cuesta:  $%.2f' %precio_compu)



