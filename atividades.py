 #1
numero = 1
while numero <= 1000:
    print(numero)
    numero += 1


#2
nomes = []
contador = 0

while contador < 10:
    nome_digitado = input(f'Digite o {contador + 1} nome: ')
    nomes.append(nome_digitado)  
    contador += 1               
    
contador = 0
while contador < 10:
    print(f'{contador + 1} - {nomes[contador]}')
    contador += 1




