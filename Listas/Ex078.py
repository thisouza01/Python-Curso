lista_valores = []

for i in range (5):
    # Recebe o valor
    try:
        valor = int(input('Valor: '))
    except ValueError:
        print('Insira um valor válido!')
        continue

    # determina posição
    if not lista_valores or valor > lista_valores[-1]:
        # coloca em último se o valor for maior que o último valor
        lista_valores.append(valor)
    else:
        # verifica se insere novo valor antes ou depois
        for posicao, numero in enumerate(lista_valores):
            if valor <= numero:
                lista_valores.insert(posicao, valor)
                break
            
print(lista_valores)