#Ejercicio 8.1. Capturar la temperatura (sea en grados Celcius o Fahrenheit) y convertirla a la escala contraria.

captura = input('Escriba la temperatura (e.g., 100°C, 32°F):')

valor, escala = float(captura[:-2]),captura[-2:]


if escala == '°C':
    fahrenheit = (valor * 9/5) + 32
    print('El valor en grados Fahrenheit es ', fahrenheit)
elif escala == '°F':
    celsius = (valor - 32) * (5/9)
    print('El valor en grados Celsius es ', celsius)
else:
    print('No ha escrito un valor de temperatura válido')


'''
# Ejercicio 1. Capturar la temperatura (sea en grados Celcius o Fahrenheit) y convertirla a la escala contraria.

# 100°C, 32°F

captura = input('Escriba la temperatura (e.g., 100°C, 32°F): ')

escala = captura[-2:]

if escala == '°C':
    valor = int(captura[:-2])
    fahrenheit = valor * 9 / 5 + 32

    print('{} es equivalante a {}°F'.format(captura, fahrenheit))
elif escala == '°F':
    valor = int(captura[:-2])
    celcius = 5/9 * (valor - 32)

    print('{} es equivalante a {}°C'.format(captura, celcius))
else:
    print('No ha escritura un valor de temperatura válido.')

'''
