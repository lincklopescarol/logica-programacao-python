print('Você está numa Calculadora, você pode '
      'fazer as 4 operações, entre elas adição (+), '
      'subtração (-), multiplicação (*) e divisão (/)')
print('Pressione S para sair.')

while True:
    operacao = input('Qual operação deseja realizar?')
    if operacao == '+' or operacao == '-' or operacao == '*' or operacao == '/':
        primeiro = int(input('Digite o primeiro valor: '))
        segundo = int(input('Digite o segundo valor: '))

    if (operacao == '+'):
        resposta = primeiro + segundo
        print('Resultado: {} + {} = {}'.format(segundo, primeiro, resposta))
        continue
    elif(operacao == '-'):
        resposta = primeiro - segundo
        print('Resultado: {} - {} = {}'.format(segundo, primeiro, resposta))
        continue
    elif (operacao == '*'):
        resposta = primeiro * segundo
        print('Resultado: {} * {} = {}'.format(segundo, primeiro, resposta))
        continue
    elif (operacao == '/'):
        resposta = primeiro / segundo
        print('Resultado: {} / {} = {}'.format(segundo, primeiro, resposta))
        continue
    elif (operacao == 'S'):
        break
    else:
        print('Operação inválida')
print('Encerrando o programa...')