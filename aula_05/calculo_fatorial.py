def valida_inteiro(pergunta, minimo, maximo):
    dado = int(input(pergunta))
    while((dado < minimo) or (dado > maximo)):
        dado = int(input(pergunta))
    return dado

def fatorial(numero):
    """
     Função que calcula o fatorial
    :param numero: número inteiro
    :return: retorna o fatorial
    """
    fatorial = 1
    if numero == 0:
        return fatorial
    for i in range(1, numero+1, 1):
        fatorial *= i
    return fatorial

valor = valida_inteiro('Digite um valor para calcular o fatorial: ', 0, 99999)
print('{}! = {}'.format(valor, fatorial(valor)))
help(fatorial)