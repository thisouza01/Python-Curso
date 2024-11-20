# ler um angulo e mostrar o sen, cos e tan

from math import radians, sin, cos, tan

angulo = float(input('Digite um angulo: '))

seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))

print('Cosseno do ângulo {} é {:.2f}'.format(angulo, cosseno))
print('Seno do ângulo {} é {:.2f}'.format(angulo, seno))
print('Tangente do ângulo {} é {:.2f}'.format(angulo, tangente))