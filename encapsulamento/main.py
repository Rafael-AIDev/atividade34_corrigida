from classe import *
# esse * é para não ficar colocando cl. 
if __name__ == '__main__':
    # entrada de dados
    nome = input('Informe o nome: ')
    idade = int(input('Informe a idade: '))
    email = input('Informe o email: ')

    # instancia da classe
    usuario = Pessoa(nome, idade, email)

    # saída de dados/ chamar usuario ponto atributo
    print(f'Nome: {usuario.nome}')
    print(f'Idade: {usuario.idade}')
    print(f'Email: {usuario.email}')