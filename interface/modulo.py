# importando a biblioteca para criação das classes abstratas
from abc import ABC, abstractmethod

# classe abstrata, que irá funcionar como uma interface
class Conta(ABC):
    # interface só possui métodos
    @abstractmethod
    def consultar_saldo(self):
        pass

    @abstractmethod
    def fazer_deposito(self, valor):
        pass

    @abstractmethod
    def fazer_saque(self, valor):
        pass

# subclasse conta corrente/tipo uma herança
class ContaCorrente(Conta):
    def __init__(self, nome, cpf, agencia, conta, saldo):
        self.__nome = nome
        self.__cpf = cpf
        self.__agencia = agencia
        self.__conta = conta
        self.__saldo = saldo
        super().__init__()
# propert é o get e o setter é o set
    #getter
    @property
    def nome(self):
        return self.__nome

    # setter
    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def cpf(self):
        return self.__cpf

    @cpf.setter
    def cpf(self, cpf):
        self.__cpf = cpf

    @property
    def agencia(self):
        return self.__agencia

    @agencia.setter
    def agencia(self, agencia):
        self.__agencia = agencia

    @property
    def conta(self):
        return self.__conta

    @conta.setter
    def conta(self, conta):
        self.__conta = conta

    @property
    def saldo(self):
        return self.__saldo

    @saldo.setter
    def saldo(self, saldo):
        self.__saldo = saldo

    # métodos da classe abstrata
    def consultar_saldo(self):
        return self.__saldo

    def fazer_deposito(self, valor):
        self.__saldo += valor
        return self.__saldo
    
    def fazer_saque(self, valor):
        self.__saldo -= valor
        return self.__saldo







