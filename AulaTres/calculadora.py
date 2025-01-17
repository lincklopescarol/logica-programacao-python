print('Você está numa Calculadora, você pode fazer as 4 operações, entre elas adição, '
      'subtração, multiplicação e divisão')
print('Pressione outra tecla para sair.')

operacao = input('Qual operação deseja realizar?')
if operacao == '+' or operacao == '-' or operacao == '*' or operacao == '/':
    primeiro = int(input('Digite o primeiro valor: '))
    segundo = int(input('Digite o segundo valor: '))

if (operacao == '+'):
    resposta = primeiro + segundo
    print('Resultado: {} + {} = {}'.format(segundo, primeiro, resposta))
elif(operacao == '-'):
    resposta = primeiro - segundo
    print('Resultado: {} - {} = {}'.format(segundo, primeiro, resposta))
elif (operacao == '*'):
    resposta = primeiro * segundo
    print('Resultado: {} * {} = {}'.format(segundo, primeiro, resposta))
elif (operacao == '/'):
    resposta = primeiro / segundo
    print('Resultado: {} / {} = {}'.format(segundo, primeiro, resposta))
else:
    print('Operação inválida')