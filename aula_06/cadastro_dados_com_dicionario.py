cadastro = {'nome': [], 'cidade': [], 'ano' :[]}

while True:
    terminar_cadastro = input('Deseja cadastrar uma pessoa? [S/N]')
    if terminar_cadastro.upper() in 'N':
        break

    nome = input('Qual o nome? ')
    cidade = input('Qual sua cidade? ')
    ano = int(input('Qual seu ano de nascimento? '))

    cadastro['nome'].append(nome)
    cadastro['cidade'].append(cidade)
    cadastro['ano'].append(ano)

lista_idades = []
lista_idades_menor_que_trinta = []
lista_idades_acima_media = []

for ano in cadastro['ano']:
    idade = (2025 - ano)
    lista_idades.append(idade)

numero_cadastros = len(cadastro['nome'])
soma_idades = sum(lista_idades)
media_idades = soma_idades // numero_cadastros

for idade, nome in zip(lista_idades, cadastro['nome']):
    if idade < 30:
        lista_idades_menor_que_trinta.append(nome)

    if idade > media_idades:
        lista_idades_acima_media.append(nome)

print('Os cadastros: ', cadastro)
print('O número de cadastros: ', numero_cadastros)
print('A média das idades é: ', media_idades)
print('A lista de pessoas com menos de 30 anos é: ', lista_idades_menor_que_trinta)
print('A lista de pessoas com idade acima da média é: ', lista_idades_acima_media)





