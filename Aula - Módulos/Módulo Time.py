import time
time.localtime() #Exibe hora local ou registros de hora

hora = time.localtime().tm_hour
print hora

tempo = time.localtime()
minuto = tempo.tm_min

print minuto

print('Transação realizada as '+ str(hora) + 'h e ' + str(minuto) + ' minutos. ')

#time.clock() Cronometro

def cont_tempo():
    inicio = time.clock()
    input ('Escreva seu nome: ')
    fim = time.clock()
    tempo = round(fim - inicio,2)
    print('Você levou '+ str(tempo) + 'segundos para escrever o seu nome')
