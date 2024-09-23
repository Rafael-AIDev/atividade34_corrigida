from dataclasses import dataclass

@dataclass
class Pessoa:
    # NOTE: atributos/ aqui está forçando um tipo no dado, JAVAliza as coisas. Forma de tipar os atributos, no app tem que colocar os valores tipo Pessoa(Alex, 39, 1.72), não serve para muita coisa
    nome: str
    idade: int
    altura: float

    def __str__(self):
        return f'Olá, meu nome é {self.nome}, tenho {self.idade} e {self.altura} metros de altura'
    
    # destrutor
    def __del__(self):
        return f'{self.nome} destruído com sucesso'