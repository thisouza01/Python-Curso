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
#ler um num de 0 a 9999 e mostrar cada digito Ex: 1234 4unidade, 3dezena, 2centena, 1milhar string e matematicamente
#ler o nome da cidade e mostra se comeca com a plavra SANTO
#ler o nome e se tem SILVA no nome
#ler uma frase e mostra quantidade de letra 'a', qual a primeira vez que aparece e a posição da umtima vez em que aparece
#ler um nome completo e mostre o primeiro e o ultimo nome
