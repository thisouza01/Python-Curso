# ler quantidade de KM rodado e quantidade de fias que foi utilizado
# calcular o preço que tem que pagar, sabendo que diaria do carro 60,00
# 0,15 reais por km rodado

kmRodado = float(input('Quantos km dirigiu? '))
diasRodado = int(input('Quantos dias andou com o carro? '))

# o valor do carro é a quantidade de dias que andou, vezes o valor da diaria
valorCarro = diasRodado * 60
valorGasolina = kmRodado * 0.15

valorTotal = valorCarro + valorGasolina

print('Dias rodados: {}, Km rodados: {}'.format(diasRodado, kmRodado))
print('Valor do aluguel: R${}, valor da gasolina: R${}'.format(valorCarro, valorGasolina))
print('Valor total é {}'.format(valorTotal))