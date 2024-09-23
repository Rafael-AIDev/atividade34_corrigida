from dataclasses import dataclass

@dataclass
class Pessoa:
    # atributos/ aqui está forçando um tipo no dado, JAVAliza as coisas. Forma de tipar os atributos, no app tem que colocar os valores tipo Pessoa(Alex, 39, 1.72), não serve para muita coisa
    nome: str
    idade: int
    altura: float

    def __str__(self):
        