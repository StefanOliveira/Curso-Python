#Tuplas são imutaveis - Listas podem ser editadas

#exercicio Tupla
meses = ('janeiro','fevereiro','março','abril','maio','junho','julho','agosto','setembro','outubro','novembro','dezembro')
data_nasc = input('Digite sua data de nascimento no formato DD-MM-AAAA: ')
indice = int(data_nasc[3:5])-1
mes = meses[indice]

print('Você nasceu no mês de ',mes)
