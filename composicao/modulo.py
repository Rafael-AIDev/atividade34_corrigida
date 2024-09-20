class Endereco:
    def __init__(self, cep, uf, cidade, bairro): 
        self.__cep = cep
        self.__uf = uf
        self.__cidade = cidade
        self.__bairro = bairro

    @property
    def cep(self):
        return self.__cep

    @cep.setter
    def cep(self, cep):
        self.__cep = cep

    @property
    def uf(self):
        return self.__uf

    @uf.setter
    def uf(self, uf):
        self.__uf = uf

    @property
    def cidade(self):
        return self.__cidade

    @cidade.setter
    def cidade(self, cidade):
        self.__cidade = cidade

    @property
    def bairro(self):
        return self.__bairro

    @bairro.setter
    def bairro(self, bairro):
        self.__bairro = bairro

    # método de ação 
    def obter_endereco(self):
        return f"{self.__bairro}, cidade de {self.__cidade}, {self.__uf}. CEP: {self.__cep}."
    
class Pessoa:
    def __init__(self, nome, idade, endereco):
        self.__nome = nome
        self.__idade = idade
        self.__endereco = endereco # composição, uma pessoa depende de um endereço, mas o endereço não depende de uma pessoa, a relação é unilateral

    # método de acesso
    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def idade(self):
        return self.__idade

    @idade.setter
    def idade(self, idade):
        self.__idade = idade

    @property
    def endereco(self):
        return self.__endereco

    @endereco.setter
    def endereco(self, endereco):
        self.__endereco = endereco

    # método de ação
    def obter_info_pessoal(self):
        return f"{self.__nome}, {self.__idade} anos, mora em {self.__endereco.obter_endereco()}." # obter endereço é método de ação da classe Endereco, um método de uma classe serve como atributo de outra classe 

class Telefone: # deslocar a classe telefone para antes da classe pessoa, porque o Python a ordem importa e o telefone estará em composição com a pessoa
    def __init__(self, telefone_comercial, telefone_pessoal, pessoa):
        self.__telefone_comercial = telefone_comercial 
        self.__telefone_pessoal = telefone_pessoal
        self.__pessoa = pessoa # composição exite a pessoa depois existe o telefone, nesse contexto

    # método de acesso
    @property
    def telefone_comercial(self):
        return self.__telefone_comercial

    @telefone_comercial.setter
    def telefone_comercial(self, telefone_comercial):
        self.__telefone_comercial = telefone_comercial

    @property
    def telefone_pessoal(self):
        return self.__telefone_pessoal

    @telefone_pessoal.setter
    def telefone_pessoal(self, telefone_pessoal):
        self.__telefone_pessoal = telefone_pessoal

    @property
    def pessoa(self):
        return self.__pessoa

    @pessoa.setter
    def pessoa(self, pessoa):
        self.__pessoa = pessoa

    # método de ação
    def obter_telefone(self):
        return f"{self.__pessoa.obter_info_pessoal()}, telefone pessoal: {self.__telefone_pessoal}, telefone comercial: {self.__telefone_comercial}."
        
        

 
    