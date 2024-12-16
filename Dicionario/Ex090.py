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

# caso tenha CTPS, pergunte o ano que foi contratado e o salario
if dado_pessoal['CTPS'] == 0:
    print(dado_pessoal)
else:
    # atualiza dicionario
    dado_pessoal.update({
        'idade': idade,
        'data_contratacao': int(input('Ano contratação: ')),
        'salario': float(input('Salario: '))
    })

    # considerando 35 anos para aposentar
    tempo_aposentar = dado_pessoal['data_contratacao'] + 35
    
    # quantidade de anops faltantes
    tempo_restante = tempo_aposentar - ano_atual

    print(dado_pessoal)
    print()
    print(f'O tempo para se aposentar é de {tempo_restante} anos')