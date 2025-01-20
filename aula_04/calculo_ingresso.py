pessoa = 0
dinheiro = 0

while True:
    idade = input('Qual sua idade?')
    if idade == 'sair':
        break
    idade = int(idade)
    pessoa += 1

    if idade < 3:
        ingresso = 0
    else:
        if idade == 12:
            ingresso = 30
        else:
            ingresso = 15
    dinheiro += ingresso

media = dinheiro / pessoa
print('Total de pessoas: {}'.format(pessoa))
print('Total de arrecadado: {}'.format(dinheiro))
print('Média arrecadada: {}'.format(media))