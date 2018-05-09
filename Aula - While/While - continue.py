x = 0
usuarios = []

while x < 4:
    nome = input('Digite o nome dos usuários: ')
    if nome == 'joao': #Sair do loop caso nome for igual a joao
        continue
    usuarios.append(nome)
    x += 1

print(usuarios)
