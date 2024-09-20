from modulo import *

if __name__ == "__main__":
    # instancia dos objetos
    endereco_pessoal = Endereco('','','','')
    usuario = Pessoa('',0,'')
    telefone = Telefone(0,0,'')

    # o endereço tem que existir, o sistema tem que existir já no sistema, buscar na base dos correios primeiro, depois cadastrar a pessoa, ele consegue o endereço por meio de uma API dos Correios, a leitura é feita por arquivos JSON, pesquisar máscara de entrada, e

    # entrada de dados 
    usuario.nome = input("Informe o nome do usuário: ")
    usuario.idade = int(input("Informe a idade do usuário: "))

    # composição usuário-endereço, esse método de já logo compor é melhor para o consumo de memória
    usuario.endereco = endereco_pessoal

    # entrada de dados do endereço
    usuario.endereco.cep = input('Informe o CEP: ')
    usuario.endereco.uf = input('Informe a UF: ')
    usuario.endereco.cidade = input('Informe a cidade: ')
    usuario.endereco.bairro = input('Informe o bairro: ')
   
    # saída de dados
    print(usuario.obter_info_pessoal())

    # composição pessoa/usuário e telefone
    telefone.usuario = telefone

    # entrada de dados 
    telefone.usuario.telefone_comercial = int(input('Informe o telefone comercial: '))
    telefone.usuario.telefone_pessoal = int(input('Informe o telefone pessoal: '))

    # saída de dados
    print(usuario.obter_telefone())
    
