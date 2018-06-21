#Programa para casa de tintas (Baseado nos exercicios do python.org)
#Um litro pinta até 3 metros de um local

nQtdMts = float(input('Informe a area em metros que será pintada: '))
nLitrosLtx = nQtdMts / 3.00 #Calculo de litros vs Metros 
nLatasLtx = float(nLitrosLtx / 18.00) #Quantidade em Litros de cada Lata de Latex
nLtxPrc = float(80.00)


if (nLitrosLtx % 18 != 0):
    nLatasLtx += 1

print ('Você precisa de: {:.0f}'.format(nLatasLtx) + ' latas de 18 litros de tinta')
print ('Total a pagar: R${:.2f}'.format(nLatasLtx * nLtxPrc))
