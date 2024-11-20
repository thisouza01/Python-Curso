# ler o comprimento do cateto oposto e do cateto adjacente de um triangulo retangulo e calcule o comprimento da hipotenusa

from math import sqrt
catetoOposto = float(input('Digite o cateto oposto: '))
catetoAdjascente = float(input('Digite o cateto adjascente: '))

hipotenusa = sqrt(catetoOposto * catetoOposto + catetoAdjascente * catetoAdjascente)

print('A hipotenusa é {:.1f}'.format(hipotenusa))