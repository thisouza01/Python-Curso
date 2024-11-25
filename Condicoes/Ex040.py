# base do exercicio dos triangulos
# equilatero = todos lados iguais
# isoceles = dois lados iguais
# escaleno = todos os lados diferentes

reta1 = int(input('Digite o tamanho da primeira reta: '))
reta2 = int(input('Digite o tamanho da segunda reta: '))
reta3 = int(input('Digite o tamanho da terceira reta: '))

if (reta1 + reta2 > reta3) and (reta2 + reta3 > reta1) and (reta1 + reta3 > reta2):
    print('A soma de dois lados é maior que o terceiro lado! É um triangulo')
    if reta1 == reta2 and reta2 == reta3:
        print('Triangulo equilatero')
    elif (reta1 == reta2 and reta2 != reta3) or (reta3 == reta2 and reta1 != reta2) or (reta3 == reta1 and reta2 != reta3):
        print('Triangulo isoceles')
    elif (reta1 != reta2 and reta1 != reta3 and reta2 != reta3):
        print('Triangulo escaleno')        
else:
    print('A soma de dois lados não é maio que o terceiro lado. Não é um triangulo')    
