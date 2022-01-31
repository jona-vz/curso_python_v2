#Ejercicio 5.2: Invertir el contenido de una tupla.
# Solución Jona:
print('Solución Jona:')
pares = (2,4,6,8,10,12,14,16,18,20)
pares_invertida = [0,0,0,0,0,0,0,0,0,0]
j=0
for i in range(len(pares)- 1, -1, -1):
    print('Índice: {} - Valor: {}'.format(i, pares[i]))
    pares_invertida[j] = pares[i]
    j += 1

pares_invertida_tupla = tuple(pares_invertida)
print(pares_invertida_tupla)


'''
# Ejercicio 5.2: Invertir el contenido de una tupla.

# (1, 2, 3, 4, 5)
# (5, 4, 3, 2, 1)

numeros = (1, 2, 3, 4, 5)
print(numeros)

print()

# Solución 1:
print('Solución 1:')
numeros_invertidos = []

for i in range(len(numeros) - 1, -1, -1):
    numeros_invertidos.append(numeros[i])

numeros_invertidos = tuple(numeros_invertidos)
print(numeros_invertidos)

print()

# Solución 2:
print('Solución 2:')
numeros_invertidos = tuple(reversed(numeros))
print(numeros_invertidos)
'''