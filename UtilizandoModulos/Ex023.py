#ler o nome e ver se tem SILVA no nome

nome = str(input('Digite um nome: '))

nomeSilva = nome.count('SILVA')

if nomeSilva > 0:
    print('Tem SILVA no nome')
else:
    print('Nao tem SILVA no nome digitado')    