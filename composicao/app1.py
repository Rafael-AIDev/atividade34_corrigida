from modulo1 import *

if __name__ == "__main__":
    # entrada de dados do usuário
    usuario = Pessoa('', 0, Endereco('', '', '', ''))

    # entrada de dados
    usuario.nome = input("Informe o nome do usuário: ")
    usuario.idade = int(input("Informe a idade do usuário: "))

    # entrada de dados do endereço
    usuario.endereco.cep = input('Informe o CEP: ')
    usuario.endereco.uf = input('Informe a UF: ')
    usuario.endereco.cidade = input('Informe a cidade: ')
    usuario.endereco.bairro = input('Informe o bairro: ')
    
    # saída de dados
    print(usuario.obter_info_pessoal())

    # entrada de dados do telefone
    telefone_comercial = input('Informe o telefone comercial: ')
    telefone_pessoal = input('Informe o telefone pessoal: ')

    # criar a instância de Telefone associando ao usuário
    telefone = Telefone(telefone_comercial, telefone_pessoal, usuario)

    # saída de dados
    print(telefone.obter_telefone())
