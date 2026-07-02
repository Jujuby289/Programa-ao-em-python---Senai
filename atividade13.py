import random

#1 
def numes():
  print('-- 1 numero aleatorio --')
  n = random.randrange(5,10)
  print('=', n)
  print('')

numes()

#2
print('-- 3 numeros aleatorios --')
for i in range(3):
    numero = random.randint(1, 100)
    print('->',numero)
print('')


#3
print('-- numero aleatorios de 10 a 30 --')
aleatorio1 = random.randrange(10,30)
print('=',aleatorio1)
print('')

#4
for i in range(10, 0, -1):
    print('->', i)
print("fogo!")
print('')


#5
print('soma de numeros pares')
usuario = int(input('insira um numero -> '))
soma = 0

for y in range(2, usuario + 1):
    if y % 2 == 0:
     soma += y

print(f'a soma do numeros pares de -> {usuario} é: = {soma}')
print('')

#6
print(' -- taboada --')
num = int(input('digite um numero: '))

for x in range(1, 11 ):
   taboada = num * x
   print(f'{num} x {x} = {taboada}')
print('')

#7
print('-- numeros impares --')
for inp in range(99, 1, -2):
    print('->', inp)
    print('')