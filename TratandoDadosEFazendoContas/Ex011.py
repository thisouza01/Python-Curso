# ler um salario e calcule um aumento de 15%

salario = float(input('Digite seu salário: '))

# aumento do salario
aumento = 0.15
novoSalario = salario + (salario * aumento)

print('Antigo salario era {} e o novo salario é {}'.format(salario, novoSalario))