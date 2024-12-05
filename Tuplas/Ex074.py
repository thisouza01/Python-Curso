tupla = ('Pao', 1, 'Bolacha', 3, 'cafe', 5, 'Leite', 10)

# mostrar formato tabulado
print('='*40)
for i in range(0, len(tupla), 2):
    item = tupla[i]
    preco = tupla[i + 1]
    print(f'Item: {item:<15} ......... R$ {preco:>3}')