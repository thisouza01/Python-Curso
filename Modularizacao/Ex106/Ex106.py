import moeda
# usar no programa principal
valor = float(input('Valor: '))

# metade
print(f'A metade de {moeda.moeda(valor)} é {moeda.metade(valor, True)}')

# dobro
print(f'O dobro de {moeda.moeda(valor)} é {moeda.dobro(valor, True)}')

# aumento de 10%
print(f'Um aumento de 10% no valor de {moeda.moeda(valor)} é {moeda.aumento(valor, True)}')

# redução de 13%
print(f'Uma diminuição de 13% no valor de {moeda.moeda(valor)} é {moeda.reducao(valor, True)}')

