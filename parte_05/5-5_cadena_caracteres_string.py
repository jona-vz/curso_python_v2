#tipo de dat compuesto String

nombre =  'Jona Vasquez'
email = "jona@gmail.com"

direccion = '''Toribio martinez #2
infonavit magisterial
juchitan de zaragoza, oaxaca'''

print(type(nombre))
print(nombre)

print()
mensaje = 'Bienvenido(a) '+ nombre + '. Correo: ' + email
print(type(mensaje))
print(mensaje)


print()
#interpolacion 
mensaje = f'Bienvenido(a) {nombre}. Correo: {email}'
print(mensaje)

#format() de la clase str
mensaje = 'Bienvenido(a) {}. Correo: {}'.format(nombre, email)
print(mensaje)

#formato con %
mensaje = 'Bienvenido(a) %s. Correo: %s'%(nombre, email)
print(mensaje)


#INMUTABILIDAD DE CADENAS DE CARACTERES (str)
lenguaje = 'python'
print(lenguaje)
print(lenguaje[0])
print(lenguaje[1])
print(lenguaje[2])
print(lenguaje[3])
print(lenguaje[4])
print(lenguaje[5])

lenguaje = 'P' + lenguaje[1:]
print(lenguaje)


#inmutables ---> estáticos

print(id('Python') == id('python'))

lenguaje = 'pYTHon'.lower()
print(lenguaje)


#USO DEL METODO str.split
valores = '2,3,5,7,11'
numeros = valores.split(',')
print(len(numeros))
print(numeros)
print(type(numeros[0]))


#USO DEL METODO str.find
indice =  valores.find('2')
print('El indice del elemento "2" es igual a ', indice)
indice =  valores.find('1')
print('El indice del elemento "1" es igual a ', indice)
indice =  valores.find('8')
print('El indice del elemento "8" es igual a ', indice)

print()
#creacion de una funcion (proceso) personalizado para buscar una cadena dentro de otra

def encontrar (cadena, caracter):
    indice = -1
    for i in range(0, len(cadena)):
        if caracter == cadena[i]:
            indice = i
            break
    return indice


indice = encontrar (valores, '2')
print('El indice del elemento "2" es igual a ', indice)
indice = encontrar (valores, '1')
print('El indice del elemento "1" es igual a ', indice)
indice =  encontrar (valores, '8')
print('El indice del elemento "8" es igual a ', indice)


