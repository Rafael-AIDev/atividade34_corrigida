# classe
class Pessoa:
    def __init__(self, nome, idade, email):
      #  self.nome = nome #public
      #  self._idade = idade #protected
      # self.__email = email #private
      self.__nome = nome
      self.__idade = idade
      self.__email = email
       # método get nome
    @property
    def nome(self):
        return self.__nome

    # método set nome
    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    # método get nome
    @property
    def idade(self):
        return self.__idade

    # método set nome
    @idade.setter
    def idade(self, idade):
        self.__idade= idade

    # método get nome
    @property
    def email(self):
        return self.__email

    # método set nome
    @email.setter
    def email(self, email):
        self.__email = email   

''' método de acesso são intermediaria para pegar os atributos, os métodos tem que ser feitos na classe

    # métodos de acesso
    def get_nome(self):
       return self.__nome
    
    def set_nome(self, nome):
       self.__nome = nome

    def get_idade(self):
       return self.__idade
    
    def set_idade(self, idade):
       self.__idade = idade

    def get_email(self):
       return self.__email
    
    def set_email(self, email):
       self.__email = email
 tem que fazer os dois metodos, pegar para definir'''

# esse método acima não está correto, os dados ainda não estão seguros

    