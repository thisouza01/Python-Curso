#ler um num de 0 a 9999 e mostrar cada digito Ex: 1234 4unidade, 3dezena, 2centena, 1milhar string e matematicamente
numInteiro = int(input('Digite um numero entre 0 e 9999: '))

unidade = numInteiro // 1 % 10
dezena = numInteiro // 10 % 10
centena = numInteiro // 100 % 10
milhar = numInteiro // 1000 % 10

print('Milhar: {} \n Centena: {} \n Dezena: {} \n Unidade: {}'.format(unidade, dezena, centena, milhar))    
