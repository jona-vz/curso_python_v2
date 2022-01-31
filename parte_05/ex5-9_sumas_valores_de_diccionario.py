#Ejercicio 5.9: Sumar todos los valores de un diccionario.

productos = {'Mouse': 29.9, 'Teclado': 119.9, 'Audifonos': 35.9, ' Monitor': 299}
total = 0.0
for v in productos.values():
    total += v

print('El total de los productos es:', total)



'''
# Ejercicio 5.9: Sumar todos los valores de un diccionario.

productos = {'Mouse': 29.9, 'Teclado': 119.9, 'Audífonos': 35.9, 'Monitor': 299}

total = sum(productos.values())

print('El total de los productos es:', total)
'''