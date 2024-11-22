#ler o nome completo e mostrar maiusculo e minusculo, quantas letras sem espaço e quantas letras tem o primeiro nome
nomeCompleto = str(input('Digite seu nome completo: '))

# maiuscula e minuscula
nomeMaiusculo = nomeCompleto.upper()
nomeMinusculo = nomeCompleto.lower()

print('Nome maiusculo: {}'.format(nomeMaiusculo))
print('Nome minusculo: {}'.format(nomeMinusculo))

# conta quantidade de espaços e o tamanho da string inteira e subtrai uma pela outra
quantidadeEspaco = nomeCompleto.count(' ')
tamanhoNome = len(nomeCompleto)

quantidadeSemEspaco = int(tamanhoNome - quantidadeEspaco)

print('Quantidade de caracteres sem espaço é: {}, e com espaço é: {}'.format(quantidadeSemEspaco, tamanhoNome))

# quantidade letra primeiro nome
nomeDivido = nomeCompleto.split()
tamanhoPrimeiroNome = len(nomeDivido[0])

print('Quantidade de caracteres do primeiro nome é: {}'.format(tamanhoPrimeiroNome))
