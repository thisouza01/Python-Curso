# calcular valorPago
# ler preco normal, condPagamento
# à vista dinheiro/cheque = 0.10
# à vista cartao = 0.05
# ate 2x cartao = precoNoraml
# 3x ou mais = + 0.20

precoNormal = float(input('Digite o preço: '))

# formas de pagamento
print('Dinheiro, Cheque, Cartão 1x, 2x, 3x(com juros)')
condPagamento = str(input('Forma de pagamento? '))


if condPagamento.lower() == 'dinheiro' or condPagamento.lower() == 'cheque':
    # calcula desconto
    valorPago = precoNormal - (precoNormal * 0.10)
    print('O valor com desconto é de {} reais'.format(valorPago))
elif condPagamento.lower() == 'cartão 1x':
    # calcula desconto
    valorPago = precoNormal - (precoNormal * 0.05)
    print('O valor com desconto é de {} reais'.format(valorPago))
elif condPagamento.lower() == 'cartão 2x':
    print('Não temos desconto, valor normal: {} reais'.format(precoNormal)) 
elif condPagamento == 'cartão 3x':
    # calcula juros
    valorPago = precoNormal + (precoNormal * 0.20)
    print('O valor com juros é de {} reais'.format(valorPago))       