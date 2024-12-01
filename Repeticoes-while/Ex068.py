somaPreco = 0
qntProduto = 0

menorPreco = float('inf')


while True:
    nome = str(input('Nome: '))
    preco = float(input('Preço: '))

    cadastrar = str(input('Quer cadastrar outro produto [s \ n] ?'))

    # total gasto
    somaPreco += preco 

    # produtos mais de 1000 reais
    if preco >= 1000:
        qntProduto += 1

    # nome produto mais barato
    if preco < menorPreco: 
        menorPreco = preco
        nomeMenor = nome

    # condição de saida
    if cadastrar == 'n':
        print(f'O total gasto foi de {somaPreco}')
        print(f'Tem {qntProduto} produtos custando mais de 1000 reais')
        print(f"O produto mais barato é {nomeMenor} e custa R${menorPreco:.2f}")
        break