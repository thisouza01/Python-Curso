# ler altura e largura e calcular sua area e a tinta necessaria sabendo que cada litro pinta uma area de 2 metros

altura = float(input('Qual a altura da parede? '))
largura = float(input('Qual a largura da parede? '))

# AreaRetangulo = base x altura
area = largura * altura
print('A area da parede é {}'.format(area))
print('----------------------')

# quantas latas de tinta
# uma lata preenche 2 metros da parede
lataTinta = 2
qntLata = int(area // lataTinta)
print('A quantidade de latas necessarias é {}'.format(qntLata))