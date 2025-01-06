import moeda
# usar no programa principal
valor = float(input('Valor: '))

# resumo -> valor, aumento e redução
moeda.resumo(valor, 20, 40)

# metade
print(f'A metade de {moeda.moeda(valor)} é {moeda.metade(valor, True)}')

# dobro
print(f'O dobro de {moeda.moeda(valor)} é {moeda.dobro(valor, True)}')