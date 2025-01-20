class Cao:
    # atributo
    familia = 'Canidae'

    # colocando o tipo int
    def __init__(self, idade: int):
        self.idade: int = idade

rex = Cao(5)
# fornece o nome da classe
print(f'Rex é um objeto de qual classe? Resposta: {rex.__class__.__name__}')