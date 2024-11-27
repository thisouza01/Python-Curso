somaIdade = 0
cntIdade = 0
listaHomem = []

for i in range(4):
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo (M \ F): '))

    # soma das idades
    somaIdade = somaIdade + idade

    # verifica idade das mulheres
    if sexo == 'F':
        if idade < 20:
            cntIdade += 1
    # verifica idade dos homens        
    elif sexo == 'M':
        listaHomem.append(idade)

# homem mais velho
maisVelho = max(listaHomem)        

# media das idades
media = somaIdade / 4

print('A soma das idades é {}.\nO homem mais velho tem {} anos.\n Tem {} mulher com menos de 20 anos'.format(media, maisVelho, cntIdade))        