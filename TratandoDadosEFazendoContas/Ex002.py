# ler algo digitado e mostrar seu tipo primitivo e todas as informações sobre

algo = input('Digite algo:')

# mostra seu tipo
print('Seu tipo é: ', type(algo))

# mostra se é numerico
print('É numérico?')
print(algo.isnumeric())
print('----------------')

# mostra se é alfanumerico
print('É alfanumérico?')
print(algo.isalnum())
print('----------------')

# mostra se é alfabetico
print('É alfabetico?')
print(algo.isalpha())
print('----------------')

# mostra se está minúsculo
print('Está em minúsculo')
print(algo.islower())
print('----------------')

# mostra se está em maiúsculo
print('Está em maiúsculo')
print(algo.isupper())