import random
def valida_inteiro(pergunta, minimo, maximo):
    dado = int(input(pergunta))
    while((dado < minimo) or (dado > maximo)):
        dado = int(input(pergunta))
    return dado

def valida_vencedor(jogador_um, jogador_dois):
    global empate, numero_vitorias_jogador_um, numero_vitorias_jogador_dois
    if jogador_um == 1:
        if jogador_dois == 1:
            empate += 1
        elif jogador_dois == 2:
            numero_vitorias_jogador_dois += 1
        elif jogador_dois == 3:
            numero_vitorias_jogador_um += 1
    elif jogador_um == 2:
        if jogador_dois == 1:
            numero_vitorias_jogador_um += 1
        elif jogador_dois == 2:
            empate += 1
        elif jogador_dois == 3:
            numero_vitorias_jogador_dois += 1
    elif jogador_um == 3:
        if jogador_dois == 1:
            numero_vitorias_jogador_dois += 1
        elif jogador_dois == 2:
            numero_vitorias_jogador_um += 1
        elif jogador_dois == 3:
            empate += 1
    resultados = [numero_vitorias_jogador_um, numero_vitorias_jogador_dois, empate]
    return resultados

print('Jogo pedra, papel e tesoura!')
print('1 - Pedra.')
print('2 - Papel.')
print('3 - Tesoura.')
print('0 - Sair do jogo.')

resultados = []
jogadas = []
numero_vitorias_jogador_um = 0
numero_vitorias_jogador_dois = 0
empate = 0

while True:
    jogador_um = valida_inteiro('Escolha sua jogada: ', 0, 3)
    if jogador_um == 0:
        break
    jogador_dois = random.randint(1, 3)
    jogadas.append([jogador_um, jogador_dois])
    resultados = valida_vencedor(jogador_um, jogador_dois)

    for jogada in jogadas:
        for dado in jogada:
            print(dado, end=' ')
        print()

print('Número de vitórias do Jogador 1: {}'.format(resultados[0]))
print('Número de vitórias do Jogador 2: {}'.format(resultados[1]))
print('Número de empates 2: {}'.format(resultados[2]))


