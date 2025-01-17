class Cao:
    # é padrão adicionar o self e depois adicionar os parâmetros do construtor
    def __init__(self, idade):
        self.idade = idade


rex = Cao(10)
print(f'A idade de Rex é: {rex.idade}')

caramelo = Cao(5)
print(f'A idade de Caramelo é: {caramelo.idade}')