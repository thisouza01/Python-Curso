# ler anoNascimento
# vai se alistar, ja é hora de se alsitar, ja passou do tempo de alistamento
# mostrar tempo que passou e tempo que falta
import datetime

anoNasc = int(input('Digite o ano do seu nascimento: '))

# obtendo a data atual
data_atual = datetime.date.today()

# ano atual
anoAtual = data_atual.year

# obtendo idade
idade = int(anoAtual - anoNasc)

# verificando serviço militar
if idade == 18:
    print('Você está no ano de prestar serviço militar!')
elif idade < 18:
    # obtem anos faltando
    anosFaltando = 18 - idade
    print('Falta {} anos para você prestar serviço militar'.format(anosFaltando))    
elif idade >= 18:
    # obtem anos passados
    anosPassado = idade - 18
    print('Você passou {} anos da idade para prestar serviço militar'.format(anosPassado))
