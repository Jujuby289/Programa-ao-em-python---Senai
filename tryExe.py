#1
try:
    nome = int(input('digite sua idade:'))
except:
    print('voce nao digitou numeros')

#2
try:
   n1 = int(input('digite um numero: '))
   n2 = int(input('digite outro numero: '))
   calculo = n1 / n2
   print(calculo)

except ZeroDivisionError as erro:
    print('nao pode dividir por zero ->', erro)

#3

