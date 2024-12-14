# recebe dados pessoais
dado_pessoal = {
    "nome": str(input('Nome: ')),
    "ano_nascimeto": int(input('Ano nascimento: ')),
    "CTPS": int(input('Carteira de Trabalho: (0 caso nao tenha) '))
}

# caso tenha CTPS, pergunte o ano que foi contratado e o salario
if dado_pessoal['CTPS'] == 0:
    print(dado_pessoal)
else:
    dado_pessoal.update({
        'data_contratacao': int(input('Ano contratação: ')),
        'salario': float(input('Salario: '))
    })
    print(dado_pessoal) 

