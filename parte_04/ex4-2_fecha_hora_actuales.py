'''
Ejercicio 4.2: Mostrar en pantalla la fecha y hora actuales del sistema.
'''
import datetime

ahora = datetime.datetime.now()

print('Fecha y hora actuales: ', ahora)
print(type(ahora))
print()

ahora_format = ahora.strftime('%H:%M:%S   %Y/%m/%d')
print(ahora_format)