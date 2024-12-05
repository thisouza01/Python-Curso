tupla = ('abacaxi', 'maca', 'pera', 'limao', 'caqui')

for item in tupla:
    print()
    for letra in item:
        if letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u':

            print(f'A palavra {item} tem as vogais {letra}')