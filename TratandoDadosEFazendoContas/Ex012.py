# ler uma temperatura em graus celsius e converter para fahrenhiet

tempGraus = float(input('Qual a temperatura atual em graus Celsius? '))

# transformando os graus
tempFahrenheit = tempGraus * 1.8 + 32

print('A temperatura atual é {}°C e convertida para Fahrenheit é {}°F'.format(tempGraus, tempFahrenheit))