# NOTE : cria a classe
class Pessoa:
    #  os atributos são sempre definidos dentro do método construtor
    # NOTE : método cosntrutor
    def __init__(self, nome, idade, cpf, email):
        self.nome = nome 
        self.idade = idade 
        self.cpf = cpf 
        self.email = email
# trecho para ser usado na atividade 36
#    def cumprimentar(self, nome, humor):
#       if humor:
#           return f'Olá {nome}, meu nome é {self.nome}. Prazer em te conhecer, {nome}.'
#       else:
#           return f'Não enche, {nome}'

# NOTE: programa principal
if __name__ == '__main__':
    # entrada de dados
    nome = input('Informe o nome do usuário: ')
    idade = int(input('Informe a idade do usuário: '))
    cpf = input('Informe o cpf do usuário: ')
    email = input('Informe o e-mail do usuário: ')

    # instancia o objeto
    usuario = Pessoa(nome, idade, cpf, email)

    # saída de dados
    print(f'Nome: {usuario.nome}.')
    print(f'Idade: {usuario.idade}.')
    print(f'CPF: {usuario.cpf}.')
    print(f'Email: {usuario.email}.')