#1
try:
    nome = int(input('digite sua idade ->'))
except:
    print('-voce nao digitou numeros-')
else:
    print('obrigado!!:D')

#2
try:
   n1 = int(input('digite um numero: '))
   n2 = int(input('digite outro numero: '))
   print(n1/n2)

except ZeroDivisionError as erro:
    print('nao pode dividir por zero ->', erro)

except ValueError:
    print('-voce nao digitou um numero:c-' )

finally:
    print('obrigado!!:D')


#3
try:
  lista = ['','1 - arroz', '2 - feijao','3 - batata', ' 4 - uva']

  print(lista)
  l1 = int(input('ecolha um produto:'))
  p = lista.index
  print('voce escolheu a',lista[l1])

except ValueError as erro:
    print('-voce nao digitou um numero!!-' )

except  IndexError as erro:
    print('-o numero esta nao lista!!-' )

finally:
    print('volte sempre!!:D')

