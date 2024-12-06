lista_valores = []

for i in range(5):
    lista_valores.append(int(input('Valor: ')))

valor_max = max(lista_valores)
print(f'O valor máximo da lista é {valor_max} e sua posição é {lista_valores.index(valor_max)}')

valor_min = min(lista_valores)
print(f'O valor mínimo da lista é {valor_min} e sua posição é {lista_valores.index(valor_min)}')