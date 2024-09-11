import classes as cl

if __name__ == '__main__':
    nome = input('Inforne o nome do usuario: ')
    email = input('Inforne o email do usuario: ')
    cpf = input('Inforne o CPF do usuario: ')
    profissao = input('Inforne a profissão do usuario: ')
    endereco = input('Inforne o endereço do usuario: ')
    telefone = input('Inforne o telefone do usuario: ')

     # instancia as classe pessoa fisica, ordem é a do construtor
    usuario = cl.PessoaFisica(nome, cpf, profissao, endereco, email, telefone)

    # entrada de dados, pode sobresscrever o endereço e o nome tipo para nome1
    nome = input('Informe o nome da empresa: ')
    email = input('Informe o email da empresa: ')
    cnpj = input('Informe o CNPJ da empresa: ')
    razao_social = input('Informe o Razão Social da empresa: ')
    endereco = input('Informe o endereço da empresa: ')
    telefone = input('Informe o telefone da empresa: ')

    # instancia a classe pessoa juridica
    empresa = cl.PessoaJuridica(nome, razao_social, cnpj, endereco, email, telefone)

    # saída de dados 
    usuario.mostrar_cartao_visitas()
    print('-'*30)
    empresa.mostrar_cartao_visitas()
     