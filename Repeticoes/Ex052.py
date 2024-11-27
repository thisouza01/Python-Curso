from datetime import date

# ano atual
anoAtual = date.today().year

# quantidade de pessoas menores de 18 anos
cntMenor = 0

for i in range(7):
    anoNascimento = int(input('Digite a data de nascimento: '))
    if anoAtual - anoNascimento < 18:
        cntMenor = cntMenor + 1

# quantidade de pessoas maiores de 18 anos
cntMaior = 7 - cntMenor

print('A quantidade de pessoas menores de 18 anos é {} e a quantidade de pessoas maiores de 18 anos é {}'.format(cntMenor, cntMaior))