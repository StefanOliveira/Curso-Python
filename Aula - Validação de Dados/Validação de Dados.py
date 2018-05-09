repetir = 's'
fatura = []
total = 0
valid_preco = False

while repetir == 's':
    produto = input('Digite o nome do produto: ')

    #Validar preço
    while valid_preco == False:
        preco = input('Digite o preço do produto: ')
        try:
            preco = float(preco)

            if preco <= 0:
                print('Valor do produto inválido.')
            else:
                valid_preco = True

        except:
            print("Formato de preço inválido, use apenas números separados por '.'.")
    
    fatura.append([produto,preco])
    total += preco
    valid_preco = False
    repetir = input('Deseja comprar mais algum produto? (S ou N)').lower()

for i in fatura:
    print(i[0],'- R$',i[1])

print('O total da fatura é:',total)
