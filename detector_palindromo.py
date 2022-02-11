def palindromo(palabra):
    palabra = palabra.replace(' ', '')
    palabra = palabra.lower()
    palabra_invertida = palabra[::-1]
    if palabra == palabra_invertida:
        return True
    else:
        return False


def run():
    palabra = input ('Escribe una frase:   ')
    es_palindromo = palindromo(palabra)
    if es_palindromo == True:
        print('Es Palindromo')
    else:
        print('NO Es Palindromo')


if __name__ == '__main__':
    run()