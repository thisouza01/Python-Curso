'crie uma função chamada voto() que vai receber como parametro o ano de nascimento de uma pessoa'
'retornando um valor literal indicando se uma pessoa tem negado, opcional ou obrigatorio '
from datetime import date

ano_nascimento = int(input('Ano nascimento: '))

# ano atual
ano_atual = date.today().year

def voto(ano_nascimento):
    idade = ano_atual - ano_nascimento

    if idade < 18:
        print(f'Com {idade} anos. Voto negado para menores de 18 anos')
    elif idade >= 18 and idade < 65:
        print(f'Com {idade} anos. Voto obrigatório para maiores de 18 anos')
    elif idade >= 65:
        print(f'Com {idade} anos. Voto opicional para maiores de 65 anos')


voto(ano_nascimento)