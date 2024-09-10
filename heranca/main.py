# superclasse (classe pai)
class Pessoa:
    # atributos
    cidade = "Brasília"
    telefone = "(61) 988884444"
    email = "nome@gmail.com"

# subclasse (classe-filha)
class PessoaFisica(Pessoa):
    # atributos
    nome = "Fulano de tal"
    cpf = "000.111.222.333"
    peso = 50
    altura = 1.75

class PessoaJuridica(Pessoa):
    # atributos
    nome_fantasia = 'Cobra Kai'
    razao_social = 'Fulano de tal S.A'
    cnpj = '8598520001/18'

# programa principal
if __name__ == '__main__':
        #instancia dos objetos 
        usuario = PessoaFisica()
        empresa = PessoaJuridica()

        print(f'{'-'*30} DADOS DO USUÁRIO {'-'*30}\n')
        print(f'Nome do usuário : {usuario.nome}')
        print(f'CPF do usuário : {usuario.cpf}')
        print(f'Peso do usuário : {usuario.peso}')
        print(f'Altura do usuário : {usuario.altura}')
        print(f'Cidade do usuário : {usuario.cidade}')
        print(f'Telefone do usuário : {usuario.telefone}')
        print(f'Email do usuário : {usuario.email}')

        print(f'{'-'*30} DADOS DA EMPRESA {'-'*30}\n')
        print(f'Nome fantasia da empresa : {empresa.nome_fantasia}')
        print(f'Razão social da empresa : {empresa.razao_social}')
        print(f'CNPJ da empresa : {empresa.cnpj}')
        print(f'Cidade do empresa : {empresa.cidade}')
        print(f'Telefone da empresa : {empresa.telefone}')
        print(f'Email da empresa : {empresa.email}')