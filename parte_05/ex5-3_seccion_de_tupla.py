#Ejercicio 5.3: Crear una sección de una tupla usando notación de slicing (rebanado).

pares = (2,4,6,8,10,12,14,16,18,20)

for i, v in enumerate(pares):
    print('Índice: {} - Valor: {}'.format(i, v))
    
primeros_pares = pares[:5] 

print(primeros_pares)


'''
# Ejercicio 5.3: Crear una sección de una tupla usando notación de slicing (rebanado).

# (1, 2, 3, 4, 5)

numeros = (1, 2, 3, 4, 5)
print(numeros)

print()

seccion = numeros[1:4]

print(seccion)

'''