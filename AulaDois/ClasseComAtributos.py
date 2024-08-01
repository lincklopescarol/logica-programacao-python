class Cao:
    # atributo
    familia = 'Canidae'

    # colocando o tipo int
    def __init__(self, idade: int):
        self.idade: int = idade


rex = Cao(10)
print(f'A idade de Rex é: {rex.idade} e pertence a família {rex.familia}')

caramelo = Cao(5)
print(f'A idade de Caramelo é: {caramelo.idade} e pertence a família {caramelo.familia}')