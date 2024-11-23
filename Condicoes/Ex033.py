# Analisando triangulo

# para saber se as retas se tornam um triangulo
# a soma de dois lado seja maior que o terceiro lado

reta1 = int(input('Digite o tamanho da primeira reta: '))
reta2 = int(input('Digite o tamanho da segunda reta: '))
reta3 = int(input('Digite o tamanho da terceira reta: '))

if (reta1 + reta2 > reta3) and (reta2 + reta3 > reta1) and (reta1 + reta3 > reta2):
    print('A soma de dois lados é maior que o terceiro lado! É um triangulo')
else:
    print('A soma de dois lados não é maio que o terceiro lado. Não é um triangulo')    
