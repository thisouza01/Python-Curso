
# recebe valor
def metade(valor = 0, formatado = False):
    resultado = valor / 2
    return resultado if formatado is False else moeda(resultado)

def dobro(valor = 0, formatado = False):
    resultado = valor * 2
    return resultado if formatado is False else moeda(resultado)

def aumento(valor = 0, tx_aumento = 0, formatado = False):
    resultado = valor + (valor * (tx_aumento/100))
    return resultado if formatado is False else moeda(resultado)

def reducao(valor = 0, tx_reducao = 0, formatado = False):
    resultado = valor - (valor * (tx_reducao/100)) 
    return resultado if formatado is False else moeda(resultado)

def moeda(valor = 0, moeda = 'R$'):
    return f'{moeda}{valor:.2f}'.replace('.',',')

def resumo(valor = 0, tx_aumento = 0, tx_reducao = 0):
    print('='*20)
    print('       Resumo       ')
    print('='*20)
    print(f'O valor é de {moeda(valor)}')
    print(f'Com um aumento de {tx_aumento}%, o valor agora é de {aumento(valor, tx_aumento, True)}')
    print(f'Com uma redução de {tx_reducao}%, o valor agora é de {reducao(valor, tx_reducao, True)}')