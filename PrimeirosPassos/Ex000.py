# criando variáveis
nome = input('Qual é o seu nome? :')
idade = input('Qual é sua idade? :')
peso = input('Qual é o seu peso? :')

# uso do print
print(nome, idade, peso)

# mostra cada numero concatenado e soma os dois ultimos 
print(1, 3, 4 + 5)
print('***********************************')


# 3 desafios
# primeiro: ler o nome de uma pessoa e mostrar uma mensagem de boas vindas de acordo com o valor digitado.
nome_desafio = input('Qual seu nome?')
print('Bem vindo '+nome_desafio+'!')
print('===============================')

# segundo: ler o dia, mes e ano de aniversario de uma pessoa ee mostre a data formatada
dia = input('Qual o dia do seu aniversário: ')
mes = input('Qual o mês do seu aniversário: ')
ano = input('Qual o ano do seu aniversário: ')
print('seu aniversário é ', dia,'/',mes,'/',ano)
print('===============================')

# terceiro: ler dois numeros e mostrar a soma entre eles
num1 = int(input('Digite um numero: '))
num2 = int(input('Digite outro numero: '))
soma = num1 + num2

# desafio extra
#print('A soma entre ', num1, ' e ', num2, ' é: ',soma)

# outra forma
print('A soma entre {} e {} é {}'.format(num1, num2, soma))