# ler peso e altura, calcular IMC
# < 18.5 abaixo do peso
# >= 18.5 and < 25 peso ideal
# >= 25 and < 30 sobrepeso
# >= 30 and < 40 Obesidade
# >= 40 obesidade morbida

peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))

# calcula IMC
imc = peso / (altura ** 2)

# verifica status IMC
if imc < 18.5:
    print('Abaixo do peso')
elif imc >= 18.5 and imc < 25:
    print('Peso ideal')
elif imc >= 25 and imc < 30:
    print('Sobrepeso')
elif imc >= 30 and imc < 40:
    print('Obesidade')
elif imc >= 40:
    print('Obesidade mórbida')                