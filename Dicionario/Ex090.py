from datetime import date

# recebe dados pessoais
dado_pessoal = {
    "nome": str(input('Nome: ')),
    "ano_nascimeto": int(input('Ano nascimento: ')),
    "CTPS": int(input('Carteira de Trabalho: (0 caso nao tenha) '))
}

# pega ano atual
ano_atual = date.today().year

# calcular idade
idade = ano_atual - dado_pessoal['ano_nascimeto']
print(idade)
print()

# caso tenha CTPS, pergunte o ano que foi contratado e o salario
if dado_pessoal['CTPS'] == 0:
    print(dado_pessoal)
else:
    dado_pessoal.update({
        'data_contratacao': int(input('Ano contratação: ')),
        'salario': float(input('Salario: '))
    })
    print(dado_pessoal) 

