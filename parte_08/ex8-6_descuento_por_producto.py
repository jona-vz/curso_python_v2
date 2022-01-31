#Ejercicio 8.6. Aplicar descuento según la cantidad de productos comprados. Cada producto cuesta $100.000.

cant = int (input('cuantos productos compraste?'))

if 1 < cant <= 3 :
    descuento = cant * 100000*.05
    total = (cant * 100000)-descuento
elif 3 < cant <= 5:
    descuento = cant * 100000*.1
    total = (cant * 100000)-descuento
elif 5 < cant <= 10:
    descuento = cant * 100000*.2
    total = (cant * 100000)-descuento
elif cant > 10:
    descuento = cant * 100000*.3
    total = (cant * 100000)-descuento

print ("descuento: ", descuento)
print ("Total: ", total)


'''
# Ejercicio 8.6. Aplicar descuento según la cantidad de productos comprados. Cada producto cuesta $100.000.

cantidad = int(input('Digite la cantidad de productos comprados: '))

if cantidad > 0:
    total = cantidad * 100000

    if 5 <= cantidad <= 20:
        total *= 0.99
    elif 20 < cantidad <= 50:
        total *= 0.97
    elif 50 < cantidad <= 100:
        total *= 0.93
    elif cantidad > 100:
        total *= 0.90

    print('El total a pagar es igual a ${}'.format(total))
else:
    print('Ha digitado una cantidad inválida.')
'''