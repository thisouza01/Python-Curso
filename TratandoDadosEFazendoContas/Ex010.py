# ler o preco e mostrar um desconto de 5%

preco = float(input('Digite o valor: '))

# desconto
desconto = 0.05
novoValor = preco - (desconto * preco)

print('O preço antigo é {} e o preço com desconto é {}'.format(preco, novoValor))