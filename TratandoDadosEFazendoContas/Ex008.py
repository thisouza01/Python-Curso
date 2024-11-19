# ler quanto dinheiro tem e mostrar quantos dolares da para comprar - pegar cotação do dolar
# 1 dolar  -> 5,78 reais

dinheiro = float(input('Quantos reais tem? '))
cotacaoDolar = float(input('Qual a cotação do Dolar? '))

dinConvertido = dinheiro / cotacaoDolar

print('Voce tem em Dolar: {}'.format(dinConvertido))