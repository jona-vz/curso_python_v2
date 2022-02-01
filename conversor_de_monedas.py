def conversor (tipo_pesos, valor_dolar):
    pesos = float(input("Cuantos pesos " + tipo_pesos + " tienes?: "))
    dolares = pesos/valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print ("Tienes $" + dolares + " dólares")


menu = """
Bienvenido al conversor de monedas 

1.- Pesos Mexicanos
2.- Pesos colombianos
3.- Pesos argentinos

Elige una opcion: """

opcion = int (input(menu))

if opcion == 1:
    conversor("mexicanos", 21)
elif opcion == 2:
    conversor("colombianos", 3875)
elif opcion == 3:
    conversor("argentinos", 65)
else:
    print("Opcion incorrecta")