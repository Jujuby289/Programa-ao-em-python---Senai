# mercado
# variavel lista i/o sinais aritimeticos logicos
print('E-commerce X')

produtos = ['',
            '1 - HD',
            '2 - monitor',
            '3 - teclado',
            '4 - iphone 17'
            ]
valores = [0,500.0,5000.0,250.0,14000.0]

print(f'''  
{produtos[1]} R$ {valores[1]}
{produtos[2]} R$ {valores[2]}
{produtos[3]} R$ {valores[3]}
{produtos[4]} R$ {valores[4]}
 ''')
carrinho = []
total= []


produto_1 = int(input('produto: '))
produto_2 = int(input('produto: '))
produto_3 = int(input('produto: '))

carrinho.extend([produtos[produto_1], produtos[produto_2], produtos[produto_3]])
total.extend([valores[produto_1], valores[produto_2], valores[produto_3]])
print('***' * 20)
print('R$', sum(total))
print('produtos:' , carrinho)
print('obrigado volte sempre!')