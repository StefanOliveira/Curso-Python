nome = input('Digite o nome do aluno: ')
nota1 = float(input('Digite a nota da primeira prova: '))
nota2 = float(input('Digite a nota da segunda prova: '))
faltas = int(input('Digite a quantidade de faltas: '))

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

