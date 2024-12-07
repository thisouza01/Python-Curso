lista_valoes = []

while True:
    # recebe valor - infinitamente
    valor = int(input('Valor: '))

    continuar = str(input('s ou n'))

    # se nao tiver na lista, adiciona
    if valor not in lista_valoes:
        lista_valoes.append(valor) 

    # condição de saida
    if continuar == 'n':
        print(lista_valoes)
        break       

