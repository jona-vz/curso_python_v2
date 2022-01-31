nombre = 'jona'
apellido = 'vasquez'
full_name = nombre + ' ' + apellido

print ('Nombre: ', nombre)
print ('Apellido: ', apellido)
print ('Nombre completo: ', full_name)
print()
print('Tipo de dato de nombre: ', type(nombre))
print('Tipo de dato de apellido: ', type(apellido))
print('Tipo de dato de full name: ', type(full_name))

edad = 29

resultado = full_name + ' tiene ' + str(edad) + ' años '
print (resultado)

print()

resultado = '{} tiene {} años'.format(full_name, edad)
print (resultado)