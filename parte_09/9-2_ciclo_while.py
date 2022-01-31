import random

#Ciclo While

numeros = [1, 2, 3, 4, 5]

i = 0

while i<len(numeros):
    print(numeros[i])
    i +=  1

print()

#Suma de los elementos de una lista con un ciclo while: 
print('Suma de los elementos de una lista con un ciclo while: ')


i = 0 
total = 0

while i< len(numeros):
    total += numeros[i]
    i += 1

print('Total: ', total)

print()

numeros.append(6)
numeros.append(7)
numeros.append(8)
numeros.append(9)
numeros.append(10)

print('Numeros: ', numeros)

#Suma de los pares: 
print('Suma de los pares: ')

suma_pares = 0
i = 0

while i< len(numeros):
    if numeros[i] % 2 == 0:
        suma_pares += numeros[i]
    i += 1

print('Suma_pares: ', suma_pares)

print()

#Suma de los impares: 
print('Suma de los impares: ')

suma_impares = 0
i = 0

while i< len(numeros):
    if numeros[i] % 2 == 1:
        suma_impares += numeros[i]
    i += 1

print('Suma_impares: ', suma_impares)

print()
#Terminacion arbitraria de la ejecucion de un ciclo while: 
print('Terminacion arbitraria de la ejecucion de un ciclo while: ')

total = 0

# while True:
#     numero = int(input('Escriba un numero positivo (0 o menos para trerminar)'))
#     if numero <= 0:
#         break

#     total += numero

# print('Total: ', total)


print()

#Adivinar un numero -Máximo 3 intentos: 
print('Adivinar un numero -Máximo 3 intentos: ')

numero_aleatorio = random.randint(1, 15)
intentos_restantes = 3

while intentos_restantes > 0:
    numero = int(input('Adivine un numero entre el 1 y 15: '))

    if numero == numero_aleatorio:
        break
    else:
        print('NEL')
        
    intentos_restantes -= 1

if intentos_restantes != 0:
    print('GANASTE!!')
else:
    print('Sigue intentando') 
