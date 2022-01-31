#Ejercicio 8.10. Validar si tres valores numéricos pueden pertenecer al esquema de colores RGB.

r= int(input('Dame el R: '))
g= int(input('Dame el G: '))
b= int(input('Dame el B: '))

if r > 0 and g>0 and  b > 0:
    if r <256  and g<256 and  b<256:
        print('LA TERCIA PUEDE SER RGB')
    else:
        print('TODOS DEBEN SER MENORES DE 256')
else:
    print('TODOS DEBEN SER MAYORES DE 0')


'''

# Ejercicio 8.10. Validar si tres valores numéricos pueden pertenecer al esquema de colores RGB.

# RGB Rojo, Verde, Azul

rojo = int(input('Digite la cantidad de color rojo (0 - 255): '))
verde = int(input('Digite la cantidad de color verde (0 - 255): '))
azul = int(input('Digite la cantidad de color azul (0 - 255): '))

if 0 <= rojo <= 255 and 0 <= verde <= 255 and 0 <= azul <= 255:
    print('Los valores %i %i %i corresponden para el esquema RGB.' % (rojo, verde, azul))
else:
    print('Los valores %i %i %i NO corresponden para el esquema RGB.' % (rojo, verde, azul))
    
'''