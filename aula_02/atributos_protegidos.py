class Cao:
    # atributo de classe
    familia = 'Canidae'

    def __init__(self, idade: int, peso: int):
        self.idade: int = idade
        self.__peso: int = peso

    # get para idade
    def get_idade(self) -> int:
        return self.idade

    # get para peso
    def get_peso(self) -> int:
        return self.__peso

    # set para peso
    def set_peso(self, peso: int):
        self.__peso = peso

# objeto rex da classe Cao
rex = Cao(10, 45)

# uso do método set_peso p
rex.set_peso(20)

print(f'Peso de Rex: {rex.get_peso()}')
print(f'Rex é um objeto de qual classe? Resposta: {rex.__class__.__name__}')