# validação de dados

sexo = ''

while sexo != 'M' or sexo != 'F':
    sexo = str(input('Digite seu sexo "M" ou "F" '))
    if sexo == 'M' or sexo == 'F':
        print('Seu sexo é {}'.format(sexo))
        break
    else:
        print('Digite corretamente o sexo, "M" ou "F"')