def sumar (a, b):
    suma = a+b
    return suma

num_1 = float (input('dame el 1er numero:  '))
num_2 = float (input('dame el 2o numero:   '))

resultado =  sumar(num_1, num_2)

print ('La suma de {} y {} es igual a {}'.format(num_1, num_2, resultado))