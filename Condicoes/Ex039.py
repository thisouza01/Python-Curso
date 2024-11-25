# Natação
from datetime import date

anoNascimento = int(input('Digite o ano de seu nascimento: '))

# confere o dia de hoje
diaAtual = date.today()
anoAtual = diaAtual.year

# confere idade
idade = anoAtual - anoNascimento

# verifica nível
if idade <= 9:
    print('Mirim')
elif idade > 9 and idade <= 14:
    print('Infantil')
elif idade > 14 and idade <= 19:
    print('Júnior')
elif idade > 19 and idade <= 20:
    print('Sênior')    
elif idade > 20:
    print('Master')  
