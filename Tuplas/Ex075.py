tupla = ('abacaxi', 'maca', 'pera', 'limao', 'caqui', 'banana')

lista_letra = []

for item in tupla:
    print()
    for letra in item:
        if letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u':
            lista_letra.append(letra)
    print(f'A palavra {item} tem as vogais {lista_letra}')
    lista_letra = []