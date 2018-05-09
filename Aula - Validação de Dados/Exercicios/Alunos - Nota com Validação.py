nome = input('Digite o nome do aluno: ')

#Validação da nota 1
valid_nota = False
while valid_nota == False:
    nota1 = input('Digite a nota da primeira prova: ')
    try:
        nota1 = float(nota1)
        if nota1 < 0 or nota1 > 10:
            print('Nota inválida, valor deve ser entre 0 e 10')
        else:
            valid_nota = True
    except:
        print("Nota inválida, use apenas números separados por'.'(Ex: 9.5)")

#Validação da nota 2
valid_nota = False
while valid_nota == False:
    nota2 = input('Digite a nota da segunda prova: ')
    try:
        nota2 = float(nota1)
        if nota2 < 0 or nota2 > 10:
            print('Nota inválida, valor deve ser entre 0 e 10')
        else:
            valid_nota = True
    except:
        print("Nota inválida, use apenas números separados por'.'(Ex: 9.5)")

#Validar faltas
valid_faltas = False
while valid_faltas == False:
    faltas = input('Digite a quantidade de faltas: ')
    try:
        faltas = int(faltas)
        if faltas > 20:
            print('Verifique o valor digitado, caso as faltas sejam superiores a 20 o aluno é automáticamente reprovado.')
        else:
            valid_faltas = True
    except:
        print("Valor incorreto, digite apenas números inteiros (Ex: 9, 15)")			


media = (nota1+nota2)/2
assid = (20-faltas)/20

if media >= 6 and assid >= 0.7:
    resultado = 'Aprovado'

elif media < 6 and assid < 0.7:
    resultado = nome,'Reprovado por média e por faltas!'

elif media < 6:
    resultado = nome,'Reprovado por média!'
    
elif assid < 0.7:
    resultado = nome,'Reprovado por faltas!'

else:
    print('Erro')

print('Nome: ',nome)
print('Media: ',media)
print('Assiduidade: ',str(assid*100)+'%')
print('Resultado: ',resultado)
