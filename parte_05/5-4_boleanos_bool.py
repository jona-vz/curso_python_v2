#boleanos 
#   False -> Falso
#   True -> verdadero

llueve = False
print(type(llueve))
print(llueve)

if llueve:
    print(' el dia esta lluvioso')
else:
    print('el dia esta espléndido')

llueve = not llueve 
print(type(llueve))
print(llueve)


if llueve:
    print(' el dia esta lluvioso')
else:
    print('el dia esta espléndido')


#OPERACIONES CON VALORES BOLEANOS  (LOGICOS)
llave_1 = True
llave_2 = False

#operadores logicos: and (conjuncion - y), or (disyuncion - o)
print(llave_1 and llave_2)
print(llave_1 and not llave_2)
print(llave_1 or llave_2)
print(not llave_1 or llave_2)


print()
if llave_1 and not llave_2:
    print ('si hay agua')
else:
    print ('no hay agua')    


print()
if not llave_1 or llave_2:
    print ('si hay agua')
else:
    print ('no hay agua')    


print()
print('USO DE LA CLASE bool()')
x= bool(1)
print(type(x))
print(x)

print()
x= bool(123)
print(type(x))
print(x)

print()
x= bool(-123)
print(type(x))
print(x)

print()
x= bool(0)
print(type(x))
print(x)

print()
x= bool(False)
print(type(x))
print(x)

print()
x= bool(True)
print(type(x))
print(x)

print()
x= 123<124
print(type(x))
print(x)

print()
x= 123>124
print(type(x))
print(x)


