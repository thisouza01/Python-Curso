tupla = ('Botafogo', 'Palmeiras', 'Flamengo', 'Internacional', 'Fortaleza', 'São Paulo', 'Corinthians', 'Bahia', 'Cruzeiro', 'Vitória', 'Grêmio', 'Vasco', 'Atlético-MG', 'Athletico-PR', 'Juventude', 'Fluminense', 'Criciúma', 'Bragantino', 'Cuiabá', 'Atlético-GO')

time = 'Chapecoense'

# cinco primeiros
for item in range(0, 5):
    print(tupla[item])

print()    

# ultimos quatro
for item in range(len(tupla) - 4, len(tupla)):
    print(tupla[item])

print()

# ordenado em ordem alfabética
ordenado = sorted(tupla)
print(ordenado)

print()

# posição 'Chapecoense'
if time in tupla:
    posicao = tupla.index(time)
    print(tupla[posicao])    
else:
    print('Não está na lista')