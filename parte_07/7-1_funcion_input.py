#entrada de datos (input) Funcion incorporada input():

print("entrada de datos (input) Funcion incorporada input():")

try:
    nombre = input('Digite su nombre: ')

    print(type(nombre).__name__)
    print(nombre)
except EOFError:
    print('El usuario cancelo la introduccion')
    print('El nombre de la persona no se guardo')
print('El programa termino')