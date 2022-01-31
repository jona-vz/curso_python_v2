#Ejercicio 8.2. Pedir al usuario que adivine un número. Sólo un intento.

import random

dado = random.randint(1,6)
print(dado)

numero = int(input ("adivina el numero del dado: "))

if numero == dado:
    print ("Correcto")
else:
    print("Sigue participando")




'''
# Ejercicio 8.2. Pedir al usuario que adivine un número. Sólo un intento.

import random

aleatorio = random.randint(1, 10)

print('Adivine un número entre 1 y 10')

numero = int(input('Escriba un número: '))

if numero == aleatorio:
    print('¡Has ganado! ¡Muy bien!')
else:
    print('No ha adivinado el número. El númera era %i.' % aleatorio)
    
'''