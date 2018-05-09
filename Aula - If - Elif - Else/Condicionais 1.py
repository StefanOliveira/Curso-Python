idade = int(input('Digite a sua idade: '))

if idade >= 18:
    print('Você é maior de 18, conteúdo liberado! ')
    print('O código a seguir será repetido infinitamente, aperte ctrl+c para interromper a execução')
    while idade >= 18:
        print('Código infinito!')

elif idade == 17:
    print('Quase lá, retorne daqui a alguns meses!')

else:
    print('Você ainda é menor de idade, conteúdo bloqueado!')
