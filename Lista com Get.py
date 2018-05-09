cores = {'vermelho': 'Red', 'verde': 'Green', 'preto': 'Black', 'rosa': 'Pink', 'amarelo': 'yellow', 'azul': 'Blue', 'branco': 'White'}
cor = input('Escolha a cor que deseja traduzir: ').lower()
traducao = cores.get(cor, 'Está cor não consta no meu dicionário')
print(traducao)
