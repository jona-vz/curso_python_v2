#NUMEROS COMPLEJOS

num_complex = 2-3j

print('Contenido de la variable num_complex:  ', num_complex)
print('El tipo de dato de la variabe num_complex es:  ', type(num_complex))

num_complex =  complex(8, 6)
print('Contenido de la variable num_complex:  ', num_complex)
print('El tipo de dato de la variabe num_complex es:  ', type(num_complex))


print()
print('OPERACIONES ARITMETICAS CON NUMEROS COMPLEJOS')

suma = 2-3j + (1+5j)
print ('Suma', suma)

resta = 2-3j - complex(1, 5)
print ('Resta', resta)

mult = 2-3j * complex(1, 5)
print ('Multiplicacion', mult)

div = 2-3j / complex(1, 5)
print ('Division', div)
