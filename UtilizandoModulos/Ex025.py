#ler um nome completo e mostre o primeiro e o ultimo nome

nomeCompleto = str(input('Digite seu nome completo: '))

nomeDividido = nomeCompleto.split(' ')
primeiroNome = nomeDividido[0]
ultimoNome = nomeDividido[-1]

print('O primeiro nome é {} e o ultimo é {}'.format(primeiroNome, ultimoNome))