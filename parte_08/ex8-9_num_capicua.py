#Ejercicio 8.9. Comprobar si un número es capicúa.

num = input ('Dame un numero: ')

numr = num[::-1]
#int(str(123456789)[::-1])
if num == numr:
    print('EL NUMERO ES COPICUA')
else:
    print('EL NUMERO NO ES COPICUA')


'''
Numero = int(input('Digite un número entero positivo: '))

if numero >= 0:
    
    if str(numero) == str(numero)[::-1]:
        print('%i es capicúa.' % numero)
    else:
        print('%i no es capicúa.' % numero)

else:
    print('El número debe ser positivo.')
'''