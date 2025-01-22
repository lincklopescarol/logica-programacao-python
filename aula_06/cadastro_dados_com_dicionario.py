cadastro = {'nome': [], 'cidade': [], 'ano' :[]}

while True:
    terminar_cadastro = input('Deseja cadastrar uma pessoa? [S/N]')
    if terminar_cadastro.upper() in 'N':
        break
    if terminar_cadastro.upper() not in 'S':
        print('Digite S para Sim ou N para Não.')
        break

    nome = input('Qual o nome? ')
    cidade = input('Qual a cidade? ')
    ano = int(input('Qual o ano de nascimento? '))

    cadastro['nome'].append(nome)
    cadastro['cidade'].append(cidade)
    cadastro['ano'].append(ano)

print(cadastro)



