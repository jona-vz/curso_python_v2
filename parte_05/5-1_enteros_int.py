#numeros 


puntaje = 300
x=-5

print (type(puntaje))
print (type(x))


print ('valor de puntaje antes de la adicion es %i' %puntaje)
puntaje = puntaje + 50
print ('valor de puntaje despues de la adicion es %i' %puntaje)
print(type(puntaje))

print()
print ('valor de x antes de la adicion es %i' %x)
x += 10
print ('valor de x despues de la adicion es %i' %x)
print('tipo de dato de la variable x es %s' %type(puntaje))

print()
print('USO DE LA CLASE int() PARA CREAR NUMEROS ENTEROS')

edad=int(input('escriba su edad '))
print('tipo de dato de la variable entrada es %s' %type(edad))


dias_vividos = edad*365
print(dias_vividos)