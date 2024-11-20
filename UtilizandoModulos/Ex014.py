# ler um numero real e mostrar sua porção inteira 

from math import trunc
numReal = float(input('Digite um numero real: '))

numInteiro = trunc(numReal)

print('Numero em sua forma inteira: {}'.format(numInteiro))