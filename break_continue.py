def run():
    # for contador in range(100):
    #     if contador % 2 != 0:
    #         continue
    #     print(contador)

    # for i in range(100):
    #     print(i)
    #     if i == 84:
    #         break

    texto = input('Escribe un texto: ')
    for letra in texto:
        if letra == 'o':
            break 
        print(letra)

if __name__ == '__main__':
    run()