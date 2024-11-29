contador = 0
media = 0

lista = []

while True:
    numero = int(input('Numero: '))
    contador += 1
    lista.append(numero)

    continuar = str(input('Quer continuar? S \ N \n'))

    if continuar != 'S':
        media = sum(lista) / contador
        maiorNum = max(lista)
        menorNum = min(lista)

        print('A media dos valores é {}\nO maior numero é {}\nO menor numero é {}'.format(media, maiorNum, menorNum))
        break 
