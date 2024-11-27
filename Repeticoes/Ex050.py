# Números primos
numero = int(input('Digite um numero: '))
qntDivisores = 0

for i in range(1, (numero + 1)):        
  if numero % i == 0:
    qntDivisores += 1
    
if qntDivisores  == 2 :
  print('primo')
else:
  print('nao primo')