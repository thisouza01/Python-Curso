# aumentos multiplos

salario = float(input('Digite seu salario: '))

if salario > 1250:
    novoSalario = salario + (salario * 0.10)
    print('Seu novo salario é {}'.format(novoSalario))
else:
    novoSalario = salario + (salario * 0.15)
    print('Seu novo salario é {}'.format(novoSalario))

