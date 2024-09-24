# importa o dataclass
from dataclasses import dataclass

# criar a classe pessoa
@dataclass # são privados e já recebem os métodos get e setter
class Pessoa:
    codigo: int
    nome: str 
    cpf: str
    email: str
    profissao: str

    # destrutor
    def __del__(self):
        return f'Objeto {self.nome}  de código {self.codigo} destruído.'