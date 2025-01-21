# cadastro de jogos e manipulação de arquivos txt

def valida_inteiro(pergunta, minimo, maximo):
    dado = int(input(pergunta))
    while((dado < minimo) or (dado > maximo)):
        dado = int(input(pergunta))
    return dado

def cria_arquivo(nome_arquivo):
    try:
        arquivo_para_criar = open(nome_arquivo, 'wt+')
        arquivo_para_criar.close()
    except:
        print('Erro na criação do arquivo.')
    else:
        print('Arquivo {} foi criado com sucesso!\n'. format(nome_arquivo))

def existe_arquivo(nome_arquivo):
    try:
        arquivo_para_abrir = open(nome_arquivo, 'rt')
        arquivo_para_abrir.close()
    except FileNotFoundError:
        return False
    else:
        return True

def cadastrar_jogo(nome_arquivo, nome_jogo, nome_videogame):
    try:
        arquivo_para_abrir = open(nome_arquivo, 'at')
    except:
        print('Erro ao abrir o arquivo.')
    else:
        arquivo_para_abrir.write('{}; {}\n'.format(nome_jogo, nome_videogame))
    finally:
        arquivo_para_abrir.close()

def listar_arquivo(nome_arquivo):
    try:
        arquivo_para_abrir = open(nome_arquivo, 'rt')
    except:
        print('Erro ao ler o arquivo')
    else:
        print(arquivo_para_abrir.read())
    finally:
        arquivo_para_abrir.close()

arquivo = 'games.txt'
if existe_arquivo(arquivo):
    print('Arquivo já existente no computador.')
else:
    print('Arquivo não existe no computador.')
    cria_arquivo(arquivo)

while True:
    print('MENU')
    print('1- CADASTRAR NOVO ITEM.')
    print('2- LISTAR CADASTROS.')
    print('3- SAIR.')

    escolha = valida_inteiro('Escolha a opção desejada: ', 1, 3)
    if escolha == 1:
        print('Opção de cadastrar novo item selecionada...\n')
        nome_jogo = input('Nome do jogo: ')
        nome_videogame = input('Nome do videogame: ')
        cadastrar_jogo(arquivo, nome_jogo, nome_videogame)
    elif escolha == 2:
        print('Opção de listar cadastros selecionada...\n')
        listar_arquivo(arquivo)
    elif escolha == 3:
        print('Encerrando o programa...')
        break