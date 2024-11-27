listaPeso = []

for i in range(5):
    peso = float(input('Digite um peso: '))
    listaPeso.append(peso)

# verifica maior peso na lista
maiorPeso = max(listaPeso)

# verifica menor peso na lista
menorPeso = min(listaPeso)

print('O mais pesado é {} e o menos pesado é {}'.format(maiorPeso, menorPeso))
