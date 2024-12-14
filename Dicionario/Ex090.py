
dado_pessoal = {
    "nome": str(input('Nome: ')),
    "ano_nascimeto": int(input('Ano nascimento: ')),
    "CTPS": int(input('Carteira de Trabalho: (0 caso nao tenha) '))
}

if dado_pessoal['CTPS'] == 0:
    print(dado_pessoal)
else:
    dado_pessoal += "ano_contratacao": int(input('Ano de contratação: '))     
