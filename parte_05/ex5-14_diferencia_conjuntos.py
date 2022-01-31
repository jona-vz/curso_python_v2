#Ejercicio 5.14: Calcular la diferencia entre dos conjuntos.

nombres_j = {'juan', 'jorge', 'jona', 'javier', 'joaquin', 'jose', 'josue', 'jonh'}
apellidos_j = {'jimenez', 'jose', 'juarez', 'jacinto', 'jordan', 'jonh', 'jaramillo'}

diferencia = nombres_j - apellidos_j
print (diferencia)

diferencia2 = apellidos_j - nombres_j
print (diferencia2)

'''
# Ejercicio 5.14: Calcular la diferencia entre dos conjuntos.

escritorio = {'Notepad++', 'Atom', 'Eclipse', 'NetBeans', 'PyCharm'}
portatil = {'Notepad++', 'PyCharm', 'Visual Studio Code', 'IntelliJ IDEA'}

resultado = escritorio.difference(portatil)

print('Los programas que hacen falta en el computador portátil son:', resultado)

print()

resultado = portatil.difference(escritorio)
print('Los programas que hacen falta en el computador de escritorio son:', resultado)

'''