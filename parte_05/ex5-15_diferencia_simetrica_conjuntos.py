#Ejercicio 5.15: Calcular la diferencia simétrica entre dos conjuntos.

nombres_j = {'juan', 'jorge', 'jona', 'javier', 'joaquin', 'jose', 'josue', 'jonh'}
apellidos_j = {'jimenez', 'jose', 'juarez', 'jacinto', 'jordan', 'jonh', 'jaramillo'}

dif_simetrica = nombres_j.symmetric_difference(apellidos_j)
print (dif_simetrica)

dif_simetrica2 = nombres_j.symmetric_difference(apellidos_j)
print (dif_simetrica2)


'''
# Ejercicio 5.15: Calcular la diferencia simétrica entre dos conjuntos.

escritorio = {'Notepad++', 'Atom', 'Eclipse', 'NetBeans', 'PyCharm'}
portatil = {'Notepad++', 'PyCharm', 'Visual Studio Code', 'IntelliJ IDEA'}

resultado = escritorio.symmetric_difference(portatil)

print('Contenido del conjunto `resultado`:', resultado)
'''